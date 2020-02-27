from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

from django.contrib.auth import login, authenticate

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')

    username = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', "password1", "password2"]

class ProfileForm(forms.ModelForm):
    CHOICES = [('1', 'Female'), ('2', 'Male')]

    profession = forms.CharField(max_length=200)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    address = forms.CharField(max_length=200) 
    
    class Meta:
        model = Profile
        fields = ['profession','gender', 'address']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']