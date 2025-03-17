from django.shortcuts import render


def registration(request):
    return render(request, 'USERS/registration.html', context=None)

def sign_in(request):
    return render(request, 'USERS/sign_in.html', context=None)

def account(request):
    return render(request, 'USERS/account.html', context=None)