from django.db import models


class Products(models.Model):
    ID = models.IntegerField()
    NAME = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препарат'
        unique_together = ('ID', 'NAME')


class Property(models.Model):
    ID = models.IntegerField(primary_key=True)
    CODE = models.CharField(max_length=512)
    NAME = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'


class PropertyMultipleValues(models.Model):
    IBLOCK_ELEMENT_ID = models.IntegerField()
    IBLOCK_PROPERTY_ID = models.CharField(max_length=512)
    VALUE = models.CharField(max_length=512, null=True, blank=True)
    VALUE_ENUM = models.CharField(max_length=512, null=True, blank=True)
    VALUE_NUM = models.FloatField(null=True, blank=True)
    DESCRIPTION = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        verbose_name = 'Параметр с несколькими значениями'
        verbose_name_plural = 'Параметры с несколькими значениями'
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
        verbose_name_plural = 'Значения параметров'


class ProductMNN(models.Model):
    MNN_ID = models.CharField(max_length=512)
    PRODUCT_ID = models.IntegerField(blank=True, null=True)
    MNN_NAME = models.CharField('Наименование', max_length=512, blank=True, null=True)
    MNN_CODE = models.CharField('Код', max_length=512, blank=True, null=True)

    class Meta:
        verbose_name = 'Международное непатентованное наименование'
        verbose_name_plural = 'Международное непатентованное наименование'
        unique_together = ('MNN_ID', 'PRODUCT_ID')
