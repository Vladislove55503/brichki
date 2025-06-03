from django.shortcuts import render

from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from rest_framework import viewsets

from . import forms
from .models import Ad
from .forms import FilterForm
from .serializers import AdSerializer


class AdsViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.query_params.get('pk')) 


class FilterView(FormView):
    template_name = 'ads/filter.html'
    form_class = FilterForm
    success_url = reverse_lazy('ads:filter')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ads'] = Ad.objects.all().select_related(
            'brand', 'model', 'generation', 'body', 'engine_type', 
            'boost_type', 'drive', 'broken',
            )
        return context


class AdView(DetailView):
    model = Ad
    template_name = 'ads/ad.html'
    context_object_name = 'ad'