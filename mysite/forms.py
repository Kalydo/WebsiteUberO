from django import forms
<<<<<<< HEAD
from .models import User_from_my_db, ReservationForm
from datetimepicker.widgets import DateTimePicker


class ReservationsForm(forms.ModelForm):

    class Meta:
        model = ReservationForm
        fields = ('title', 'ticket_number', 'taxi_driver',
                  'from_street', 'from_street_number', 'from_plz','from_loc',
                  'to_street', 'to_street_number', 'to_plz', 'to_loc', 'order_time',
                  )

        labels = {
            'title': 'Anzahl Personen',
            'ticket_number': 'Ticketnummer',
            'taxi_driver': 'Taxifahrer',
            'from_street': 'Strasse',
            'from_street_number': 'Hausnummer',
            'from_plz': 'Postleitzahl',
            'from_loc': 'Stadt',
            'to_street': 'Strasse',
            'to_street_number': 'Hausnummer',
            'to_plz': 'Postleitzahl',
            'to_loc': 'Stadt',
            'order_time': 'Zeit',
        }


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Passwort wiederholen', widget=forms.PasswordInput)
    email = forms.EmailField(label='E-Mail')
    first_name = forms.CharField(label='Name')
    last_name = forms.CharField(label='Nachname')

    class Meta:
        model = User_from_my_db
        fields = ('username', 'email', 'first_name',
                  'last_name', 'street', 'street_number', 'city', 'plz', 'password',)
=======
from django.contrib.auth.forms import UserCreationForm

from .models import User_from_my_db, Profile
from django.contrib.auth.models import User

from django.contrib.auth import hashers


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User_from_my_db
        fields = ('username','password1', 'password2', 'email', 'first_name',
                  'last_name', 'street', 'street_number', 'city', 'plz')
>>>>>>> master

        labels = {
            'username': 'Benutzername',
            'password': 'Passwort',
            'first_name': 'Name',
            'last_name': 'Nachname',
            'email': 'E-Mail',
            'street': 'Strasse',
            'street_number': 'Hausnummer',
            'plz': 'Postleitzahl',
            'city': 'Stadt'
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if email is "":
            raise forms.ValidationError("Bitte gib eine E-Mail an", code='missing_email', )
        return email

    def clean_city(self):
        city = self.cleaned_data['city']
        if city is "":
            raise forms.ValidationError("Bitte gib eine Stadt an", code='missing_city', )
        return city

    def clean_street_number(self):
        street_number = self.cleaned_data['street_number']
        if street_number is "":
            raise forms.ValidationError("Bitte gib eine Strassennummer an", code='missing_street_number', )
        return street_number

    def clean_street(self):
        street = self.cleaned_data['street']
        if street is "":
            raise forms.ValidationError("Bitte gib eine Strasse an", code='missing_street', )
        return street

    def clean_plz(self):
        plz = self.cleaned_data['plz']
        if plz is None:
            raise forms.ValidationError("Bitte gib eine gültige Postleitzahl ein", code="missing_plz", )
        return plz

<<<<<<< HEAD
    def clean_password2(self):
        # Check that the two password entries match
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("Stimmt nicht überein")
        return password

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
=======

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
>>>>>>> master
