from datetime import timedelta

from django.utils import timezone
from rest_framework.exceptions import ValidationError

from eaptekahack.constants import EventChoices
from eaptekahack.models import EventForReminder, TreatmentCourse


class PlannedEventCreator:
    # schedule_info:
    # {
    #         "start_date": "DD.MM.YYYY", (default: текущая дата),
    #         "time": ["08:00","12:00","20:00",],
    #         "repeat_limit": {. — Предел генерации
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

    def create_events_taking_medical_drugs(self):
        self._get_planned_dates()

        events_to_create = []

        for date in self.planned_dates:
            for time in self.periodical_time:
                planned_datetime = timezone.datetime(date.year, date.month, date.day, time.hour, time.minute,)
                events_to_create.append(
                    EventForReminder(
                        planned_datetime=planned_datetime,
                        course=self.course,
                        event_code=EventChoices.TAKING_MEDICAL_DRUGS,
                    )
                )

        if events_to_create:
            EventForReminder.objects.bulk_create(events_to_create)

        self.course.save()

    def create_events_drug_is_running_out(self):
        EventForReminder.objects.create(
            planned_datetime=timezone.now() + timedelta(minutes=15),
            course=self.course,
            event_code=EventChoices.DRUG_IS_RUNNING_OUT,
        )

    def create_events_make_order(self):
        EventForReminder.objects.create(
            planned_datetime=timezone.now() + timedelta(minutes=5),
            course=self.course,
            event_code=EventChoices.MAKE_ORDER,
        )
