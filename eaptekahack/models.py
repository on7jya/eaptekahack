from django.contrib.auth.models import AbstractUser
from django.db import models


class Products(models.Model):
    ID = models.IntegerField()
    NAME = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Products'
        unique_together = ('ID', 'NAME')


class Property(models.Model):
    ID = models.IntegerField(primary_key=True)
    CODE = models.CharField(max_length=512)
    NAME = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Property'


class PropertyMultipleValues(models.Model):
    IBLOCK_ELEMENT_ID = models.IntegerField()
    IBLOCK_PROPERTY_ID = models.CharField(max_length=512)
    VALUE = models.CharField(max_length=512, null=True, blank=True)
    VALUE_ENUM = models.CharField(max_length=512, null=True, blank=True)
    VALUE_NUM = models.FloatField(null=True, blank=True)
    DESCRIPTION = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        verbose_name = 'Параметр с несколькими значениями'
        verbose_name_plural = 'PropertyMultipleValues'
        unique_together = ('IBLOCK_ELEMENT_ID', 'IBLOCK_PROPERTY_ID', 'VALUE')


class PropertyValues(models.Model):
    IBLOCK_ELEMENT_ID = models.IntegerField(unique=True)
    PROPERTY_276 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_429 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_326 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_574 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_265 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_284 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_541 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_542 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_343 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_428 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_274 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_263 = models.FloatField(blank=True, null=True)
    PROPERTY_264 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_594 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_344 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_483 = models.FloatField(max_length=512, blank=True, null=True)
    PROPERTY_536 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_540 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_356 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_567 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_332 = models.CharField(max_length=512, blank=True, null=True)
    PROPERTY_283 = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        verbose_name = 'Значения параметра'
        verbose_name_plural = 'PropertyValues'


class ProductMNN(models.Model):
    MNN_ID = models.CharField(max_length=512)
    PRODUCT_ID = models.IntegerField(blank=True, null=True)
    MNN_NAME = models.CharField('Наименование', max_length=512, blank=True, null=True)
    MNN_CODE = models.CharField('Код', max_length=512, blank=True, null=True)

    class Meta:
        verbose_name = 'Международное непатентованное наименование'
        verbose_name_plural = 'ProductMNN'
        unique_together = ('MNN_ID', 'PRODUCT_ID')


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


class MedicationReminder(models.Model):
    """
    """

    course = models.ForeignKey(
        'TreatmentCourse', on_delete=models.CASCADE, verbose_name='Курс', related_name='reminder',
    )
    planned_datetime = models.DateTimeField('Дата и время события')
