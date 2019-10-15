from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm


def home(request):
    return render(request, 'pages/index.html')


def reservation(request):
    return render(request, 'pages/Bestellung.html')


def index(request):
    return render(request, 'base.html')


def logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account erstellt für {username}!')
            return redirect('homepage')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def about(request):
    return render(request, 'pages/about.html')