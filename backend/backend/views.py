import json
from models import Valute, Rate
from django.http import JsonResponse


def get_rates(request):
    valutes = request.GET.get('valutes').split(',')
    date_start = request.GET.get('date_start')
    date_end = request.GET.get('date_end')
    results = []

    for valute in valutes:
        rates = Rate.objects.filter(valute__code=valute, date__gte=date_start, date__lte=date_end).order_by('-date')
        for rate in rates:
            results.append({
                'valute': valute,
                'date': rate.date,
                'value': rate.value,
                'nominal': rate.nominal,
            })

    return JsonResponse(results, safe=False)


def get_valutes(request):
    valutes = Valute.objects.all()
    results = []

    for valute in valutes:
        results.append({
            'code': valute.code,
            'name': valute.name,
        })

    return JsonResponse(results, safe=False)
