from django.urls import path, include
from . import views


app_name = 'users'

urlpatterns = [
    path('reg/', views.CreateUserView.as_view(), name='reg'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('account/', views.UserView.as_view(), name='account'),
    path('create_ad/', views.CreateAdView.as_view(), name='create_ad'),
    path('update_ad/<slug:pk>', views.UpdateAdView.as_view(), name='update_ad'),
    path('delete_ad/<slug:pk>', views.DeleteAdView.as_view(), name='delete_ad'),
]