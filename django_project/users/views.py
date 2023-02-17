from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm
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
    return render(request, 'users/profile.jinja2', context={'title': 'profile'})
