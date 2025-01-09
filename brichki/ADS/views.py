from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    context = dict()
    return render(request, 'base.html', context)
