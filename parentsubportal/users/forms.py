from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    CHOICES = [('1', 'Female'), ('2', 'Male')]

    email = forms.EmailField()
    profession = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'special',
        }
    ))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    address = forms.CharField() 

    class Meta:
        model = User
        fields = ["username", "email", "profession", 
        "password1", "password2", "gender", "address"]

class UserUpdateForm(forms.ModelForm):
    CHOICES = [('1', 'Female'), ('2', 'Male')]

    email = forms.EmailField()
    profession = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'special',
        }
    ))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    address = forms.CharField() 

    class Meta:
        model = User
        fields = ['username', 'email', 'profession', 'gender', 'address']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
  