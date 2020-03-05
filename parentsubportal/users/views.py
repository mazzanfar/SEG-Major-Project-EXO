from django.shortcuts import render
from .forms import SignUpForm, ProfileForm, ProfileUpdateForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def register(request):
    form = SignUpForm(request.POST)
    profile_form = ProfileForm(request.POST)

    if form.is_valid() and profile_form.is_valid():
        userMan = form.save()
        # Create a profile object without saving it yet
        profile = profile_form.save(commit=False)

        profile.user = userMan
        profile.save()

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    else:
        form = SignUpForm()
        profile_form = ProfileForm()

    return render(request, 'users/register.html', {'form': form, 'profile_form': profile_form})


# This function is garbage and has no purpose/does not work -> note: Make it better
@login_required
def profile(request):

    if request.method == 'POST':
        u_form = ProfileForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = ProfileForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
