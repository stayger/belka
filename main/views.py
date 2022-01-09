from django.shortcuts import render
from .models import Conс
from django.db.models import *


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def report(request):
    month = '1'
    if request.method == 'POST':
        month = request.POST['month']

    items = Conс.objects.filter(dt__month=month) \
        .aggregate(Min('fe'), Max('fe'), Avg('fe'),
                   Min('si'), Max('si'), Avg('si'),
                   Min('al'), Max('al'), Avg('al'),
                   Min('ca'), Max('ca'), Avg('ca'),
                   Min('s'), Max('s'), Avg('s'),
                   )
    months = range(1, 13)
    return render(request, 'main/report.html', {'items': items, 'months': months, 'mm': month})
