from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'New account is created for {username}, you can login now')
            return redirect('user-login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.jinja2', context={'form': form, 'title': 'register'})


@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            username = user_update_form.cleaned_data.get('username')
            messages.success(
                request, 'Your account has been updated')
            return redirect('user-profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.jinja2', context={'title': 'profile', 'user_update_form': user_update_form, 'profile_update_form': profile_update_form})
