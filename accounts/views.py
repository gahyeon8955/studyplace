from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from .forms import UserCreationForm

User = get_user_model()

# Create your views here.

# def signup(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.get(username=request.POST['username'])
#                 return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
#             except User.DoesNotExist:
#                 user = User.objects.create_user(
#                     request.POST['username'], password=request.POST['password1'])
#                 auth.login(request, user)
#                 return redirect('home')
#         else:
#             return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
#     else:
#         return render(request, 'accounts/signup.html')

# def signup(request):
#     form = UserCreationForm(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password1']
#             user = auth.authenticate(username = email, password = password)
#             auth.login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})

def signup(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            if form.is_valid():
                form.save()
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']
                user = auth.authenticate(username = email, password = password)
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')