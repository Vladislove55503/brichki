from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from ADS.models import Ads


def index(request):
    context = {
        'title_page': 'Brichki.ru',
        'title_center': 'filter',
        'title_right': 'catalog',
    }
    return render(request, 'ADS/main.html', context)
