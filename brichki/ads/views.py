from django.shortcuts import render

from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from rest_framework import viewsets
from rest_framework import generics

from . import forms
from .models import Ad
from .forms import FilterForm
from .serializers import AdSerializer, AdCreateSerializer


class AdListAPIView(generics.ListAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    filterset_fields = ['author',]


class AdCreateAPIView(generics.CreateAPIView):
    serializer_class = AdCreateSerializer
    queryset = Ad.objects.all()


class AdRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


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