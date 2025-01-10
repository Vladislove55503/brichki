from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    context = {
        'title_page': 'Brichki.ru',
    }
    return render(request, 'brichki/base.html', context)
