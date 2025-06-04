from django.urls import path, include

from . import views


app_name = 'ads'


urlpatterns = [
    path('', views.FilterView.as_view(), name='filter'),
    path('ad/<slug:pk>', views.AdView.as_view(), name='ad'),

    path('api_ad_create/', views.AdCreateAPIView.as_view()),
    path('api_ad_list/', views.AdListAPIView.as_view()),
]