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
            Products.objects.bulk_create([Products(**obj) for obj in json_data], batch_size=1000, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS('''Created product successfully!'''))

    def upload_property(self, *args, **options):
        with open('initial_data/property.json', newline='', encoding='utf-8-sig') as file:
            json_data = json.load(file)
            Property.objects.bulk_create([Property(**obj) for obj in json_data], batch_size=1000, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS('''Created property successfully!'''))

    def upload_property_multiple_values(self, *args, **options):
        with open('initial_data/propertyMultipleValues.json', newline='', encoding='utf-8-sig') as file:
            json_data = json.load(file)

            PropertyMultipleValues.objects.bulk_create(
                [PropertyMultipleValues(**obj) for obj in json_data], batch_size=1000, ignore_conflicts=True
            )
            remove_duplicated_records(PropertyMultipleValues, ['IBLOCK_ELEMENT_ID', 'IBLOCK_PROPERTY_ID', 'VALUE'])
        self.stdout.write(self.style.SUCCESS('Created propertyMultipleValues successfully!'))

    def upload_property_values(self, *args, **options):
        with open('initial_data/propertyValues.json', newline='', encoding='utf-8-sig') as file:
            json_data = json.load(file)

            PropertyValues.objects.bulk_create(
                [PropertyValues(**obj) for obj in json_data], batch_size=1000, ignore_conflicts=True
            )
        self.stdout.write(self.style.SUCCESS('Created propertyValues successfully!'))

    def upload_product_to_mnn(self, *args, **options):
        with open('initial_data/productToMNN.json', newline='', encoding='utf-8-sig') as file:
            json_data = json.load(file)

            ProductMNN.objects.bulk_create(
                [ProductMNN(**obj) for obj in json_data], batch_size=1000, ignore_conflicts=True
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
