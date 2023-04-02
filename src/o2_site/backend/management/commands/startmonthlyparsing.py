from django.core.management.base import BaseCommand

from backend.services.rss import start_monthly_parsing


class Command(BaseCommand):

    help = 'start monthly rss parsing'

    def handle(self, *args, **options):
        self.stdout.write('Starting monthly rss parsing')
        start_monthly_parsing()
