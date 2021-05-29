from django.contrib import admin

from eaptekahack.models import ProductMNN, Products, Property, PropertyMultipleValues, PropertyValues, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'ID',
        'NAME',
    )
    list_display_links = ('ID', 'NAME')
    ordering = ('ID',)
    search_fields = ('ID', 'NAME')


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'ID',
        'CODE',
        'NAME',
    )
    list_display_links = ('ID', 'CODE', 'NAME')
    list_filter = (
        'ID',
        'CODE',
    )
    ordering = ('ID',)
    search_fields = ('ID', 'CODE', 'NAME')


@admin.register(PropertyMultipleValues)
class PropertyMultipleValuesAdmin(admin.ModelAdmin):
    list_display = (
        'IBLOCK_ELEMENT_ID',
        'IBLOCK_PROPERTY_ID',
        'VALUE',
        'VALUE_ENUM',
        'VALUE_NUM',
        'DESCRIPTION',
    )
    ordering = ('IBLOCK_ELEMENT_ID',)
    search_fields = ('IBLOCK_ELEMENT_ID', 'IBLOCK_PROPERTY_ID', 'VALUE')


@admin.register(PropertyValues)
class PropertyValuesAdmin(admin.ModelAdmin):
    list_display = (
        'IBLOCK_ELEMENT_ID',
        'PROPERTY_276',
        'PROPERTY_429',
        'PROPERTY_326',
        'PROPERTY_574',
        'PROPERTY_265',
        'PROPERTY_284',
        'PROPERTY_541',
        'PROPERTY_542',
        'PROPERTY_343',
        'PROPERTY_428',
        'PROPERTY_274',
        'PROPERTY_263',
        'PROPERTY_264',
        'PROPERTY_594',
        'PROPERTY_344',
        'PROPERTY_483',
        'PROPERTY_536',
        'PROPERTY_540',
        'PROPERTY_356',
        'PROPERTY_567',
        'PROPERTY_332',
        'PROPERTY_283',
    )
    ordering = ('IBLOCK_ELEMENT_ID',)
    search_fields = ('IBLOCK_ELEMENT_ID',)


@admin.register(ProductMNN)
class ProductMNNAdmin(admin.ModelAdmin):
    list_display = ('MNN_ID', 'PRODUCT_ID', 'MNN_NAME', 'MNN_CODE')
    ordering = ('MNN_ID',)
    search_fields = ('MNN_ID', 'PRODUCT_ID', 'MNN_NAME', 'MNN_CODE')
