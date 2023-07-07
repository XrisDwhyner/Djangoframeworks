from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(min_length=2, max_length=225)
    last_name = forms.CharField(min_length=2, max_length=225)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
