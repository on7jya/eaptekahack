from django.utils import timezone
from rest_framework.exceptions import ValidationError

from eaptekahack.models import MedicationReminder, TreatmentCourse


class PlannedEventCreator:
    # schedule_info:
    # {
    #         "start_date": "DD.MM.YYYY", (default: текущая дата),
    #         "time": ["08:00","12:00","20:00",],
    #         "repeat_limit": {. — Предел генерации
    #             "without_date": "boolean",  — Генерировать постоянно
    #             "date": "DD.MM.YYYY",  — Генерировать до определенной даты
    #             "count": "number. — Генерировать определенное количество раз
    #         }
    #  },
    def __init__(self, course: TreatmentCourse):
        self.course = course
        self.user = course.user
        self.schedule_info = course.schedule_info

        self.start_date = self.schedule_info['start_date'] or timezone.now().date()

        self.periodical_time = course.schedule_info['time']
        if repeat_limit_date := self.schedule_info['repeat_limit'].get('date'):
            self.repeat_limit_date = repeat_limit_date
        elif repeat_limit_count := self.schedule_info['repeat_limit'].get('count'):
            self.repeat_limit_count = repeat_limit_count
        elif without_date := self.schedule_info['repeat_limit'].get('without_date'):
            self.without_date = without_date
        else:
            raise ValidationError('Требуется заполнить периодичность приема!')
        self.planned_dates = []

    def _get_planned_dates(self):
        delta = timezone.timedelta(days=1)
        planned_date = self.start_date

        while True:
            if planned_date >= self.start_date or (
                self.repeat_limit_count and self.course.number_of_events >= self.repeat_limit_count
            ):
                self.course.is_enabled_for_generation = False
                break

            self.planned_dates.append(planned_date)
            self.course.number_of_events += 1
            planned_date += delta

    def create_tasks(self):
        self._get_planned_dates()

        events_to_create = []

        for date in self.planned_dates:
            for time in self.periodical_time:
                planned_datetime = timezone.datetime(date.year, date.month, date.day, time.hour, time.minute,)
                events_to_create.append(MedicationReminder(planned_datetime=planned_datetime, user=self.user))

        if events_to_create:
            MedicationReminder.objects.bulk_create(events_to_create)

        self.course.save()
