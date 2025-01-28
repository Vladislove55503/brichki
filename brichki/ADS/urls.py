from django.urls import path
from . import views


app_name = 'ADS'

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('<int:ad_pk>', views.ad_page, name="ad_page"),
]