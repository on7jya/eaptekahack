from config import celery_app
from eaptekahack.controllers.treatment_course_controller import PlannedEventCreator
from eaptekahack.models import TreatmentCourse


@celery_app.task(ignore_result=True)
def generate_event_for_push():
    courses = TreatmentCourse.objects.filter(is_enabled_for_generation=True)

    for course in courses:
        event_creator = PlannedEventCreator(course)
        event_creator.create_tasks()
