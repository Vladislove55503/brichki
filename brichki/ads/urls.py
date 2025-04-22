from django.urls import path, include
from . import views


app_name = 'ads'

urlpatterns = [
    path('', views.FilterView.as_view()),
    path('ad/<slug:pk>', views.AdView.as_view()),
]