import csv
import io
from urllib.request import urlopen
from urllib.parse import unquote
from django.shortcuts import render
from django.http import HttpResponse
from .models import Metric

def performance(request):
    return HttpResponse("Here , we analyze performance marketing.")

def load_data(request):
    url = "https://gist.githubusercontent.com/kotik/3baa5f53997cce85cc0336cb1256ba8b/raw/3c2a590b9fb3e9c415a99e56df3ddad5812b292f/dataset.csv"
    response = urlopen(unquote(url))
    with urlopen(url) as f:
        csvfile = f.read().decode('utf-8')
        cr = csv.DictReader(csvfile.splitlines())
        for row in cr:
            _, created = Metric.objects.update_or_create(
                date = row['date'],
                channel = row['channel'],
                country = row['country'],
                os = row['os'],
                impressions = row['impressions'],
                clicks = row['clicks'],
                installs = row['installs'],
                spend = row['spend'],
                revenue = row['revenue'])
    return HttpResponse('here')