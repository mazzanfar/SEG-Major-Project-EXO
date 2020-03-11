from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.core.validators import RegexValidator

from django.contrib.auth import login, authenticate


class SignUpForm(UserCreationForm):
    alphabetvalide = RegexValidator(
        r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')

    first_name = forms.CharField(max_length=40, validators=[alphabetvalide])
    last_name = forms.CharField(max_length=40, validators=[alphabetvalide])
    email = forms.EmailField(max_length=60)

    username = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', "password1", "password2"]


class ProfileForm(forms.ModelForm):
    CHOICES = [('1', 'Female'), ('2', 'Male')]

    profession = forms.CharField(max_length=60)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    address = forms.CharField(max_length=60)
    city = forms.CharField(max_length=40)
    country = forms.CharField(max_length=40)

    class Meta:
        model = Profile
        fields = ['profession', 'gender',
                  'address', 'city', 'country', 'image']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profession', 'gender',
                  'address', 'city', 'country', 'image']
