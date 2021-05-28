from django.db import models


# Create your models here.

class Basket(models.Model):
    ORDER_ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    PRODUCT_ID = models.CharField(max_length=200)
    QUANTITY = models.FloatField
    PRICE = models.FloatField
    DETAIL_PAGE_URL = models.CharField(max_length=200)


class Orders(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    PERSON_TYPE_ID = models.IntegerField
    DATE_INSERT = models.DateTimeField
    STATUS_ID = models.CharField(max_length=1)
    LID = models.CharField(max_length=200)
    USER_ID = models.IntegerField


class Products(models.Model):
    ID = models.IntegerField(primary_key=True)
    NAME = models.CharField(max_length=200)


class Property(models.Model):
    ID = models.IntegerField(primary_key=True)
    CODE = models.CharField(max_length=200)
    NAME = models.CharField(max_length=200)


class PropertyMultipleValues(models.Model):
    IBLOCK_ELEMENT_ID = models.IntegerField(primary_key=True)
    IBLOCK_PROPERTY_ID = models.IntegerField(primary_key=True)
    VALUE = models.IntegerField(primary_key=True)
    VALUE_ENUM = models.CharField(max_length=200)  # ?????
    VALUE_NUM = models.FloatField
    DESCRIPTION = models.CharField(max_length=200)


class PropertyValues(models.Model):
    IBLOCK_ELEMENT_ID = models.IntegerField(primary_key=True)
    PROPERTY_276 = models.CharField(max_length=200)
    PROPERTY_429 = models.CharField(max_length=200)
    PROPERTY_326 = models.CharField(max_length=200)
    PROPERTY_574 = models.CharField(max_length=200)
    PROPERTY_265 = models.CharField(max_length=200)
    PROPERTY_284 = models.CharField(max_length=200)
    PROPERTY_541 = models.CharField(max_length=200)
    PROPERTY_542 = models.CharField(max_length=200)
    PROPERTY_343 = models.CharField(max_length=200)
    PROPERTY_428 = models.CharField(max_length=200)
    PROPERTY_274 = models.CharField(max_length=200)
    PROPERTY_263 = models.CharField(max_length=200)
    PROPERTY_264 = models.CharField(max_length=200)
    PROPERTY_594 = models.CharField(max_length=200)
    PROPERTY_344 = models.CharField(max_length=200)
    PROPERTY_483 = models.CharField(max_length=200)
    PROPERTY_536 = models.CharField(max_length=200)
    PROPERTY_540 = models.CharField(max_length=200)
    PROPERTY_356 = models.CharField(max_length=200)
    PROPERTY_567 = models.CharField(max_length=200)
    PROPERTY_332 = models.CharField(max_length=200)
    PROPERTY_283 = models.CharField(max_length=200)
