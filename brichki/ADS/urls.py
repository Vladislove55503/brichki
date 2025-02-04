from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'ADS'

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('<int:ad_pk>', views.ad_page, name="ad_page"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)