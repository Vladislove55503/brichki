from django.urls import path, include
from rest_framework import routers

from . import views


app_name = 'ads'


router = routers.DefaultRouter()
router.register(r'ads', views.AdsViewSet, 'ads-list')

urlpatterns = [
    path('', views.FilterView.as_view(), name='filter'),
    path('ad/<slug:pk>', views.AdView.as_view(), name='ad'),
    path('api/', include(router.urls)),
]