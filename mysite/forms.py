from django import forms
from .models import User_from_my_db
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

        labels = {
            'username': 'Benutzername',
            'password1': 'Passwort',
            'password2': 'Passwort wiederholen',
            'first_name': 'Name',
            'last_name': 'Nachname',
            'email': 'E-Mail',
        }


class UserAdditional(forms.ModelForm):

    class Meta:
        model = User_from_my_db
        fields = ('street', 'street_number', 'plz', 'city')

    labels = {
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


