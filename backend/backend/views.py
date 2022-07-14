from .models import Valute, Rate
from django.http import JsonResponse, HttpResponse, FileResponse
from django.template.loader import render_to_string
import csv
import openpyxl
import weasyprint
import os 
from django.conf import settings


def get_rates(request):
    valutes = request.GET.get('valutes').split(',')
    date_start = request.GET.get('date__gte')
    date_end = request.GET.get('date__lte')
    results = []

    for valute in valutes:
        rates = Rate.objects.filter(valute__code=valute, date__gte=date_start, date__lte=date_end)
        for rate in rates:
            results.append({
                'valute': valute,
                'date': rate.date,
                'value': round(rate.value, 2),
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


#create and attach pdf to response
def render_to_pdf(request):
    valutes = request.GET.get('valutes').split(',')
    date_start = request.GET.get('date__gte')
    date_end = request.GET.get('date__lte')

    qs = []

    #create query set
    for valute in valutes:
        rates = Rate.objects.filter(valute__code=valute, date__gte=date_start, date__lte=date_end).select_related('valute')
        for rate in rates:
            print(round(rate.value, 2))
            qs.append({
                'valute': valute,
                'valute_name': rate.valute.name,
                'date': rate.date,
                'value': round(rate.value, 2),
                'nominal': rate.nominal,
            })
    string = render_to_string('backend/templates/pdf.html', {'context': qs})
    css_string = render_to_string('backend/static/css/pdf.css')
    print(css_string)
    html = weasyprint.HTML(string=string)
    css = weasyprint.CSS(string=css_string)
    result = html.write_pdf(stylesheets=[css])

    response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="rates.pdf"'},
        )
    response.write(result)

    return response


#create and attach csv to reponse
def render_to_csv(request):
    valutes = request.GET.get('valutes').split(',')
    date_start = request.GET.get('date__gte')
    date_end = request.GET.get('date__lte')

    qs = []

    #create query set
    for valute in valutes:
        rates = Rate.objects.filter(valute__code=valute, date__gte=date_start, date__lte=date_end).select_related('valute')
        for rate in rates:
            qs.append({
                'valute': valute,
                'valute_name': rate.valute.name,
                'date': rate.date,
                'value': round(rate.value, 2),
                'nominal': rate.nominal,
            })

    print(len(qs))

    response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="rates.csv"'},
        )

    writer = csv.writer(response)
    writer.writerow(['Код валюты', 'Валюта', 'Дата', 'Цена', 'Номинал'])

    for q in qs:
        writer.writerow([q['valute'], q['valute_name'], q['date'], q['value'], q['nominal']])

    return response


#create and attach xlsx to response
def render_to_xlsx(request):
    print(request)
    valutes = request.GET.get('valutes').split(',')
    date_start = request.GET.get('date__gte')
    date_end = request.GET.get('date__lte')

    qs = []

    #create query set
    for valute in valutes:
        rates = Rate.objects.filter(valute__code=valute, date__gte=date_start, date__lte=date_end).select_related('valute')
        for rate in rates:
            qs.append({
                'valute': valute,
                'valute_name': rate.valute.name,
                'date': rate.date,
                'value': round(rate.value, 2),
                'nominal': rate.nominal,
            })

    print(len(qs))

    response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="rates.xlsx"'},
        )

    wb = openpyxl.Workbook()
    ws = wb.active

    ws.append(['Код валюты', 'Валюта', 'Дата', 'Цена', 'Номинал'])

    for q in qs:
        ws.append([q['valute'], q['valute_name'], q['date'], q['value'], q['nominal']])

    wb.save(response)

    return response
