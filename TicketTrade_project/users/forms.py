from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Children

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email'] 


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']

class ChildrenRegisterForm(forms.ModelForm):

    class Meta:
        model = Children
        fields = ['first_name', 'last_name', 'age', 'diagnosis', 'disability'] 