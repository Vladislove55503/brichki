from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from . import forms
from .models import Ad


# Create your views here.

class AdView(DetailView):
	model = Ad
	template_name = 'ads/ad.html'
	context_object_name = 'ad'

class FilterView(TemplateView):
	template_name = 'ads/filter.html'