from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from mysite.forms import UserForm, ReservationsForm, UserUpdateForm
from mysite.models import ReservationForm
import uuid


def home(request):
    return render(request, 'pages/index.html')


def reservation(request):
    if request.method == "POST":
        form = ReservationsForm(request.POST)
        if form.is_valid():
            id = uuid.uuid1()
            tablefill = ReservationForm()
            order_time = request.POST.get('time')
            title = request.POST.get('title')
            taxi_driver = request.POST.get('taxi_driver')
            ticket_number = (id.int / 1000000000000000000000000000000)
            from_street = request.POST.get('from_street')
            from_street_number = request.POST.get('from_street_number')
            from_plz = request.POST.get('from_plz')
            from_loc = request.POST.get('from_loc')
            to_street = request.POST.get('to_street')
            to_street_number = request.POST.get('to_street_number')
            to_plz = request.POST.get('to_plz')
            to_loc = request.POST.get('to_loc')
            get_user = request.user

            tablefill.user = get_user

            tablefill.order_time = order_time
            tablefill.title = title
            tablefill.taxi_driver = taxi_driver
            tablefill.ticket_number = ticket_number
            tablefill.from_street = from_street
            tablefill.from_street_number = from_street_number
            tablefill.from_plz = from_plz
            tablefill.from_loc = from_loc
            tablefill.to_street = to_street
            tablefill.to_street_number = to_street_number
            tablefill.to_plz = to_plz
            tablefill.to_loc = to_loc
            tablefill.save()
            messages.success(request, f'Bestellung mit der Nummer {ticket_number} wurde erstellt.')
            return redirect('reservation')
        else:
            messages.error(request, 'Ups da ist was vergessen gegangen :(')
            return render(request, 'pages/bestellung.html', {
                'form': form
            })
    else:
        form = ReservationsForm()
        return render(request, 'pages/bestellung.html', {
            'form': form
        })


def index(request):
    return render(request, 'base.html')


def logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Ups da ist was vergessen gegangen :(')
            return render(request, 'registration/register.html', {
                'form': form,
            })
    else:
        form = UserForm()
        return render(request, 'registration/register.html', {
            'form': form,
        })


def about(request):
    return render(request, 'pages/about.html')

@login_required
def profileinfo(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request, 'pages/profileinfo.html', context)


def profile(request):
    return render(request, 'pages/profile.html')


def profilereservation(request):
    all_records = ReservationForm.objects.filter(user_id=request.user.id)
    return render(request, 'pages/profilereservation.html', {'all_records': all_records})
