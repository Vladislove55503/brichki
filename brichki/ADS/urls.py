from django.urls import path
from . import views


urlpatterns = [
    # /ADS/
    path('', views.index, name="index"),
]