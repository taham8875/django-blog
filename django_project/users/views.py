from django.shortcuts import render
from django.contrib import messages
from users.forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'New account is created for {username}')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.jinja2', context={'form': form, 'title': 'register'})
