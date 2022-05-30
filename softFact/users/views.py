from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .forms import NewUserForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, "There was an error")
            return redirect('login')
    return render(request, 'authenticate/login.html')


def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('/')
        else:
            messages.success(request, "Unsuccessful registration. Invalid information.")
            return redirect('register')
    form = NewUserForm()
    return render(request, 'authenticate/register.html', {'register_form': form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')


def user_profile(request):
    return render(request, 'authenticate/profile.html')

def contact_us(request):
    return render(request, 'authenticate/contact_us.html')
