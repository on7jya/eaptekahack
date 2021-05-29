from django.db.models import TextChoices


class EventChoices(TextChoices):
    TAKING_MEDICAL_DRUGS = 'taking_medical_drugs', 'Прием препарата'
