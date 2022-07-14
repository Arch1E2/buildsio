from ...models import Valute, Rate
from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = 'Get valute rates'

    def get_today_rates(self):
        r = requests.get('https://api.exchangerate.host/latest?base=USD')

        return r.json()

    def handle(self, *args, **options):
        r = self.get_today_rates()
        rates = r['rates']
        date = r['date']

        for rate in rates.keys():
            Rate.objects.update_or_create(
                valute=Valute.objects.get(code=rate),
                date=date,
                value=rates[rate],
                nominal=1,
            )
            
        return "Rates at " + date + " were added"


