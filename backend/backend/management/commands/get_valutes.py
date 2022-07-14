from ...models import Valute
from django.core.management.base import BaseCommand
import requests
import json

class Command(BaseCommand):
    help = 'Get valute rates'

    def get_valutes(self):
        r = requests.get('https://api.exchangerate.host/symbols')
        data = r.json()

        return data["symbols"]

    def handle(self, *args, **options):
        valutes = self.get_valutes()
        created_valutes = 0
        for valute in valutes.keys():
            Valute.objects.update_or_create(code=valute, name=valutes[valute]['description'])
            created_valutes += 1

        return f'Created valutes: {created_valutes}'