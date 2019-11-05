from django import forms
from .models import User_from_my_db
from django.contrib.auth import hashers


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User_from_my_db
        fields = ('username', 'email', 'first_name', 'password',
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

    def clean_password2(self):
        # Check that the two password entries match
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
