import json

from django.core.management.base import BaseCommand
from django.db.models import Count, Max

from eaptekahack.models import ProductMNN, Products, Property, PropertyMultipleValues, PropertyValues


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.upload_products()
        self.upload_property()
        self.upload_property_multiple_values()
        self.upload_property_values()
        self.upload_product_to_mnn()

    def upload_products(self):
        with open('initial_data/products.json', newline='', encoding='utf-8-sig') as file:
            json_data = json.load(file)

            Products.objects.bulk_create(
                [Products(id=obj['ID'], name=obj['NAME']) for obj in json_data], batch_size=1000, ignore_conflicts=True
            )
        self.stdout.write(self.style.SUCCESS('''Created product successfully!'''))

    def upload_property(self, *args, **options):
        with open('initial_data/property.json', newline='', encoding='utf-8-sig') as file:
            json_data = json.load(file)

            Property.objects.bulk_create(
                [Property(id=obj['ID'], name=obj['NAME'], code=obj['CODE']) for obj in json_data],
                batch_size=1000,
                ignore_conflicts=True,
            )
        self.stdout.write(self.style.SUCCESS('''Created property successfully!'''))

    def upload_property_multiple_values(self, *args, **options):
        with open('initial_data/propertyMultipleValues.json', newline='', encoding='utf-8-sig') as file:
            json_data = json.load(file)

            PropertyMultipleValues.objects.bulk_create(
                [
                    PropertyMultipleValues(
                        iblock_element_id=obj['IBLOCK_ELEMENT_ID'],
                        iblock_property_id=obj['IBLOCK_PROPERTY_ID'],
                        value=obj['VALUE'],
                        value_enum=obj['VALUE_ENUM'],
                        value_num=obj['VALUE_NUM'],
                        description=obj['DESCRIPTION'],
                    )
                    for obj in json_data
                ],
                batch_size=1000,
                ignore_conflicts=True,
            )
            remove_duplicated_records(PropertyMultipleValues, ['iblock_element_id', 'iblock_property_id', 'value'])
        self.stdout.write(self.style.SUCCESS('Created propertyMultipleValues successfully!'))

    def upload_property_values(self, *args, **options):
        with open('initial_data/propertyValues.json', newline='', encoding='utf-8-sig') as file:
            json_data = json.load(file)

            PropertyValues.objects.bulk_create(
                [
                    PropertyValues(
                        iblock_element_id=obj['IBLOCK_ELEMENT_ID'],
                        property_276=obj['PROPERTY_276'],
                        property_429=obj['PROPERTY_429'],
                        property_326=obj['PROPERTY_326'],
                        property_574=obj['PROPERTY_574'],
                        property_265=obj['PROPERTY_265'],
                        property_284=obj['PROPERTY_284'],
                        property_541=obj['PROPERTY_541'],
                        property_542=obj['PROPERTY_542'],
                        property_343=obj['PROPERTY_343'],
                        property_428=obj['PROPERTY_428'],
                        property_264=obj['PROPERTY_264'],
                        property_594=obj['PROPERTY_594'],
                        property_344=obj['PROPERTY_344'],
                        property_483=obj['PROPERTY_483'],
                        property_536=obj['PROPERTY_536'],
                        property_540=obj['PROPERTY_540'],
                        property_356=obj['PROPERTY_356'],
                        property_567=obj['PROPERTY_567'],
                        property_332=obj['PROPERTY_332'],
                        property_283=obj['PROPERTY_283'],
                    )
                    for obj in json_data
                ],
                batch_size=1000,
                ignore_conflicts=True,
            )
        self.stdout.write(self.style.SUCCESS('Created propertyValues successfully!'))

    def upload_product_to_mnn(self, *args, **options):
        with open('initial_data/productToMNN.json', newline='', encoding='utf-8-sig') as file:
            json_data = json.load(file)

            ProductMNN.objects.bulk_create(
                [
                    ProductMNN(
                        mnn_id=obj['MNN_ID'],
                        product_id=obj['PRODUCT_ID'],
                        mnn_name=obj['MNN_NAME'],
                        mnn_code=obj['MNN_CODE'],
                    )
                    for obj in json_data
                ],
                batch_size=1000,
                ignore_conflicts=True,
            )
            self.stdout.write(self.style.SUCCESS('Created productToMNN successfully!'))


def remove_duplicated_records(model, fields):
    """
    Removes records from `model` duplicated on `fields`
    while leaving the most recent one (biggest `id`).
    """
    duplicates = (
        model.objects.values(*fields).order_by().annotate(max_id=Max('id'), count_id=Count('id')).filter(count_id__gt=1)
    )

    for duplicate in duplicates:
        (model.objects.filter(**{x: duplicate[x] for x in fields}).exclude(id=duplicate['max_id']).delete())
