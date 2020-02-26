from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, ProfileForm
from django.contrib.auth import login, authenticate

# Create your views here.

def home_view(request):
    return render(request, '')

def register(request):
    form = SignUpForm(request.POST)
    profile_form = ProfileForm(request.POST)

    if form.is_valid() and profile_form.is_valid():
        user = form.save()
        #Create a profile object without saving it yet
        profile = profile_form.save(commit=False)

        profile.user = user
        profile.save()

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('')
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'users/register.html', {'form': form, 'profile_form': profile_form})


@login_required
def profile(request):
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
