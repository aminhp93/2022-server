from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start update list stock'))
        self.stdout.write(self.style.SUCCESS('End update list stock'))
