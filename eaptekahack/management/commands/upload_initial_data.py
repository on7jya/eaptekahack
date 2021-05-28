from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        # TODO upload data
        self.stdout.write(self.style.SUCCESS('Successfully updated initial data!'))
