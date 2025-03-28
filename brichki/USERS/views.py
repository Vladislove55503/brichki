from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import BaseUserCreationForm


class LoginUserView(LoginView):
    template_name = 'USERS/login.html'
    next_page = 'ADS:main_page'

class RegisterUserView(CreateView):
    template_name = 'USERS/registration.html'
    form_class = BaseUserCreationForm
    success_url = reverse_lazy('ADS:main_page')

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('ADS:main_page')


def logout_user(request):
    if request.POST:
        logout(request)
        return redirect('ADS:main_page')
    else:
        return render(request, 'USERS/logged_out.html')