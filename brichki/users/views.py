from django.views.generic import (
    CreateView, UpdateView, TemplateView, DeleteView,
    )
from django.contrib.auth.views import LogoutView, LoginView 

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

from django.core.exceptions import PermissionDenied

from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import UserSerializer

from . import forms
from ads.models import Ad


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUserView(CreateView):
    template_name = 'users/reg.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('users:account')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:account')
        return super().get(request, *args, **kwargs)


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    authentication_form = AuthenticationForm
    next_page = 'users:account'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:account')
        return self.render_to_response(self.get_context_data())


class LogoutUserView(LogoutView):
    next_page = 'users:login'


@method_decorator(login_required(), name='dispatch')
class UserView(TemplateView):
    template_name = 'users/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['own_ads'] = Ad.objects.filter(
        author=self.request.user.id
            ).select_related(
            'brand', 'model', 'generation', 'body', 'engine_type', 
            'boost_type', 'drive', 'broken',
            )
        return context


@method_decorator(login_required(), name='dispatch')
class CreateAdView(CreateView):
    template_name = 'users/create_ad.html'
    form_class = forms.AdCreateForm
    success_url = reverse_lazy('users:account')

    def form_valid(self, form, *args, **kwargs):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(CreateAdView, self).form_valid(form)


@method_decorator(login_required(), name='dispatch')
class UpdateAdView(UpdateView):
    model = Ad
    template_name = 'users/update_ad.html'
    form_class = forms.AdUpdateForm
    success_url = reverse_lazy('users:account')

    def get_object(self, queryset=None):
        obj = super(UpdateAdView, self).get_object()
        
        if not obj.author == self.request.user:
            raise PermissionDenied
        return obj    

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except PermissionDenied:
            return redirect('users:account')
        
        return super().get(request, *args, **kwargs)


@method_decorator(login_required(), name='dispatch')
class DeleteAdView(DeleteView):
    model = Ad
    template_name = 'users/delete_ad.html'  
    success_url = reverse_lazy('users:account')
    
    def get_object(self, queryset=None):
        obj = super(DeleteAdView, self).get_object()

        if not obj.author == self.request.user:
            raise PermissionDenied
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except PermissionDenied:
            return redirect('users:account')
        
        return super().get(request, *args, **kwargs)