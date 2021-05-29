from django.db.models import TextChoices


class EventChoices(TextChoices):
    TAKING_MEDICAL_DRUGS = 'taking_medical_drugs', 'Прием препарата'
    EXPIRATION_DATE = 'expiration_date', 'Окончание срока годности'
    DRUG_IS_RUNNING_OUT = 'drug_is_running_out', 'Окончание запаса лекарств'
    MAKE_ORDER = 'make_order', 'Сделать до-заказ'
