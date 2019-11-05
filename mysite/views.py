from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from mysite.forms import UserForm, UserAdditional



def home(request):
    return render(request, 'pages/index.html')


def reservation(request):
    if request.method == "POST":
        von = request.POST.get('von')
        nach = request.POST.get('nach')
        messages.success(request, f'Weg von {von} nach {nach}!')
        redirect('reservation')
    return render(request, 'pages/Bestellung.html')


def index(request):
    return render(request, 'base.html')


def logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        formadd = UserAdditional(request.POST)
        if form.is_valid and formadd.is_valid():
            form.save()
            formadd.save()
            return redirect('register')
        else:
            messages.error(request, 'Ups da ist was vergessen gegangen :(')
            return render(request, 'registration/register.html', {
                'form': form,
                'formadd': formadd
            })
    else:
        form = UserForm(request.POST)
        formadd = UserAdditional(request.POST)
        return render(request, 'registration/register.html', {
            'form': form,
            'formadd': formadd
        })


def about(request):
    return render(request, 'pages/about.html')
