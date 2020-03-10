from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

from django.contrib.auth import login, authenticate

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    username = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', "password1", "password2"]

class ProfileForm(forms.ModelForm):
    CHOICES = [('1', 'Female'), ('2', 'Male'), ('3', 'Prefer not to say')]

    profession = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows':5, 'cols':90}))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    Postcode = forms.CharField(max_length=200)
    children = forms.CharField(max_length=200)

    class Meta:
        model = Profile
        fields = ['profession','gender', 'Postcode']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
     model = Profile
     fields = ['image']
