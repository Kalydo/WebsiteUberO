from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User_from_my_db, Profile
from django.contrib.auth.models import User

from django.contrib.auth import hashers


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User_from_my_db
        fields = ('username','password1', 'password2', 'email', 'first_name',
                  'last_name', 'street', 'street_number', 'city', 'plz')

        labels = {
            'username': 'Benutzername',
            'first_name': 'Name',
            'last_name': 'Nachname',
            'email': 'E-Mail',
            'street': 'Strasse',
            'street_number': 'Hausnummer',
            'plz': 'Postleitzahl',
            'city': 'Stadt'
        }

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


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']