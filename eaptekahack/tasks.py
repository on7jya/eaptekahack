from datetime import timedelta

from django.utils import timezone

from config import celery_app
from eaptekahack.constants import DRUG_IS_LOW_QUANTITY_CHOICES, EventChoices
from eaptekahack.controllers.treatment_course_controller import PlannedEventCreator
from eaptekahack.models import EventForReminder, MedicationAvailable, TreatmentCourse

COUNT_OF_EVENTS_FOR_DRUG_IS_RUNNING_OUT = 10
COUNT_OF_EVENTS_FOR_MAKE_ORDER = 3


def send_push(event, user):
    # Здесь должна быть логика по отправке пуша в пуш-сервис.
    # Т.к. фронт не успевает, то заглушка
    pass


@celery_app.task(ignore_result=True)
def generate_event_for_taking_medical_drugs():
    courses = TreatmentCourse.objects.filter(is_enabled_for_generation=True)

    for course in courses:
        event_creator = PlannedEventCreator(course)
        event_creator.create_events_taking_medical_drugs()


@celery_app.task(ignore_result=True)
def generate_event_for_drug_is_running_out():
    med_availables = MedicationAvailable.objects.filter(courses__is_active=True)

    for med_available in med_availables:
        event_creator = PlannedEventCreator(med_available.course)
        # если текущего кол-ва не хватает на 3 процедур приема, то генерим события для пуша на уведомление об окончании кол-ва препаратов
        if med_available.number_of_pills < med_available.course.quantity * COUNT_OF_EVENTS_FOR_MAKE_ORDER:
            event_creator.create_events_drug_is_running_out()
        # если текущего кол-ва не хватает на 10 процедур приема, то генерим события для пуша на дозаказ
        elif med_available.number_of_pills < med_available.course.quantity * COUNT_OF_EVENTS_FOR_DRUG_IS_RUNNING_OUT:
            event_creator.create_events_make_order()


@celery_app.task(ignore_result=True)
def send_push_reminder_taking_medical_drugs():
    # Осталось 15 минут до планового приема задачи
    time_start = timezone.now() + timedelta(minutes=14)
    time_finish = timezone.now() + timedelta(minutes=15)
    events = EventForReminder.objects.filter(
        event_code=EventChoices.TAKING_MEDICAL_DRUGS, planned_datetime__gte=time_start, planned_datetime__lt=time_finish
    )
    for event in events:
        send_push(event=event, user=event.course.user)

    # плановый прием лекарств!
    time_start = timezone.now() - timedelta(minutes=1)
    time_finish = timezone.now()
    events = EventForReminder.objects.filter(
        event_code=EventChoices.TAKING_MEDICAL_DRUGS,
        is_success=False,
        planned_datetime__gte=time_start,
        planned_datetime__lt=time_finish,
    )
    for event in events:
        send_push(event=event, user=event.course.user)


@celery_app.task(ignore_result=True)
def send_push_reminder_for_drug_is_running_out():
    # Осталось 15 минут до планового приема задачи
    time_start = timezone.now() + timedelta(minutes=14)
    time_finish = timezone.now() + timedelta(minutes=15)
    events = EventForReminder.objects.filter(
        event_code__in=DRUG_IS_LOW_QUANTITY_CHOICES, planned_datetime__gte=time_start, planned_datetime__lt=time_finish
    )
    for event in events:
        send_push(event=event, user=event.course.user)
