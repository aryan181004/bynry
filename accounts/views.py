from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomerRegistrationForm, CustomerUpdateForm
from .models import generate_account_number
from service_requests.models import ServiceRequest

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.account_number = generate_account_number()
                user.save()
                login(request, user)
                messages.success(request, 'Registration successful!')
                return redirect('home')
            except IntegrityError:
                messages.error(request, 'Registration failed. Please try again.')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def home(request):
    service_requests = []
    if request.user.is_authenticated:
        service_requests = ServiceRequest.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'accounts/home.html', {'service_requests': service_requests})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('home')
    return render(request, 'accounts/logout.html')