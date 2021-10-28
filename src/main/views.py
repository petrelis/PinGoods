from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:homepage')
        else:
            messages.info(request, 'Try again! username or password is incorrect')

    context = {}
    return render(request, 'main/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('main:login')

def home_page(request):
    return render(request, 'main/home.html')

def registrationchoice_page(request):
    return render(request, 'main/registrationchoice.html')

def customerregister_page(request):
    if request.method != 'POST':
        form = CustomUserForm()
    else:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:login')

    context = {'form': form}

    return render(request, 'main/customerregister.html', context)

def sellerregister_page(request):
    if request.method != 'POST':
        form = CustomUserForm()
    else:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:login')

    context = {'form': form}

    return render(request, 'main/sellerregister.html', context)