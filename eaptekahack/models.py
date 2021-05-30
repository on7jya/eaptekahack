from django.contrib.auth.models import AbstractUser
from django.db import models

from eaptekahack.constants import EventChoices


class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=512)
    img_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Products'


class Property(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=512)
    name = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Property'


class PropertyMultipleValues(models.Model):
    iblock_element_id = models.IntegerField()
    iblock_property_id = models.CharField(max_length=512)
    value = models.CharField(max_length=512, null=True, blank=True)
    value_enum = models.CharField(max_length=512, null=True, blank=True)
    value_num = models.FloatField(null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        verbose_name = 'Параметр с несколькими значениями'
        verbose_name_plural = 'PropertyMultipleValues'
        unique_together = ('iblock_element_id', 'iblock_property_id', 'value')


class PropertyValues(models.Model):
    iblock_element_id = models.IntegerField(unique=True)
    property_276 = models.CharField(max_length=512, blank=True, null=True)
    property_429 = models.CharField(max_length=512, blank=True, null=True)
    property_326 = models.CharField(max_length=512, blank=True, null=True)
    property_574 = models.CharField(max_length=512, blank=True, null=True)
    property_265 = models.CharField(max_length=512, blank=True, null=True)
    property_284 = models.CharField(max_length=512, blank=True, null=True)
    property_541 = models.CharField(max_length=512, blank=True, null=True)
    property_542 = models.CharField(max_length=512, blank=True, null=True)
    property_343 = models.CharField(max_length=512, blank=True, null=True)
    property_428 = models.CharField(max_length=512, blank=True, null=True)
    property_274 = models.CharField(max_length=512, blank=True, null=True)
    property_263 = models.FloatField(blank=True, null=True)
    property_264 = models.CharField(max_length=512, blank=True, null=True)
    property_594 = models.CharField(max_length=512, blank=True, null=True)
    property_344 = models.CharField(max_length=512, blank=True, null=True)
    property_483 = models.FloatField(max_length=512, blank=True, null=True)
    property_536 = models.CharField(max_length=512, blank=True, null=True)
    property_540 = models.CharField(max_length=512, blank=True, null=True)
    property_356 = models.CharField(max_length=512, blank=True, null=True)
    property_567 = models.CharField(max_length=512, blank=True, null=True)
    property_332 = models.CharField(max_length=512, blank=True, null=True)
    property_283 = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        verbose_name = 'Значения параметра'
        verbose_name_plural = 'PropertyValues'


class ProductMNN(models.Model):
    mnn_id = models.CharField(max_length=512)
    product_id = models.IntegerField(blank=True, null=True)
    mnn_name = models.CharField('Наименование', max_length=512, blank=True, null=True)
    mnn_code = models.CharField('Код', max_length=512, blank=True, null=True)

    class Meta:
        verbose_name = 'Международное непатентованное наименование'
        verbose_name_plural = 'ProductMNN'
        unique_together = ('mnn_id', 'product_id')


class User(AbstractUser):
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=16, blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class TreatmentCourse(models.Model):
    """
    schedule_info:
        {
                "start_date": "DD.MM.YYYY", (default: текущая дата),
                "time": ["08:00","12:00","20:00",],
                "repeat_limit": {. — Предел генерации
                    "date": "DD.MM.YYYY",  — Генерировать до определенной даты
                    "count": "number. — Генерировать определенное количество раз
                }
         }
    """

    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Юзер', related_name='treatment_course',)
    drug = models.ForeignKey(
        'Products', on_delete=models.CASCADE, verbose_name='Препарат', related_name='treatment_course',
    )
    schedule_info = models.JSONField('График приема лекарств', default=dict)
    quantity = models.DecimalField('Количество единиц для приема', max_digits=9, decimal_places=3)
    quantity_exists = models.DecimalField('Количество единиц в наличии', max_digits=9, decimal_places=3)
    number_of_events = models.IntegerField('Количество событий приема', blank=True, null=True)
    is_active = models.BooleanField('Активный курс?', default=True)
    is_enabled_for_generation = models.BooleanField('Генерировать события?', default=True)

    class Meta:
        verbose_name = 'Курс приема'
        verbose_name_plural = 'Курс приема'


class EventForReminder(models.Model):
    """
    События
    """

    course = models.ForeignKey(
        'TreatmentCourse', on_delete=models.CASCADE, verbose_name='Курс', related_name='reminder',
    )
    planned_datetime = models.DateTimeField('Дата и время события')
    event_code = models.CharField(
        'Инициализирующее событие', max_length=50, choices=EventChoices.choices, db_index=True
    )
    is_success = models.BooleanField('Событие успешно?', default=False)
    comment = models.TextField('Комментарий', blank=True, null=True)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class MedicationAvailable(models.Model):
    """
     вводится первоначальное значение при создании курса,
        + если совершается покупка
        - если отметил в календаре что принял
    """

    course = models.ForeignKey(
        'TreatmentCourse', on_delete=models.CASCADE, verbose_name='Курс', related_name='medication_available',
    )
    number_of_pills = models.IntegerField('Количество оставшихся таблеток на руках', blank=True, null=True)

    class Meta:
        verbose_name = 'Остаток лекарства'
        verbose_name_plural = 'Остаток лекарства'
