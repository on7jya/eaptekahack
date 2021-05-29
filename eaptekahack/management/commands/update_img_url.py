import json

from django.core.management.base import BaseCommand

from eaptekahack.models import Products


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.upload_img_url()

    def upload_img_url(self):
        with open('initial_data/basket.json', newline='', encoding='utf-8-sig') as file:
            json_data = json.load(file)
            for obj in json_data:
                product_id = obj['PRODUCT_ID']
                url = obj['DETAIL_PAGE_URL']
                Products.objects.filter(id=product_id).update(img_url=url)
        self.stdout.write(self.style.SUCCESS('''Updated img successfully!'''))
