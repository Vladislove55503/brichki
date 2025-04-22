from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView 
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.views import LogoutView 

from django.views.generic.base import TemplateView

from . import forms
from ads.models import Ad


# Create your views here.

class CreateUserView(CreateView):
	template_name = 'users/reg.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('users:account')

class LoginUserView(LoginView):
	template_name = 'users/login.html'
	authentication_form = AuthenticationForm
	next_page = 'users:account'

class LogoutUserView(LogoutView):
	next_page = 'users:login'

class UserView(TemplateView):
	template_name = 'users/account.html'

class CreateAdView(CreateView):
	template_name = 'users/create_ad.html'
	form_class = forms.AdCreateForm

class UpdateAdView(UpdateView):
	model = Ad
	template_name = 'users/update_ad.html'
	form_class = forms.AdUpdateForm
