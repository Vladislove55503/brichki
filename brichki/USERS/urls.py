from django.urls import path

from . import views


app_name = 'USERS'

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('account/', views.account, name='account'),
]