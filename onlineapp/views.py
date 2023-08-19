from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def signup(request):
    context = {}

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('conf-pass') 
        profile_picture = request.POST.get('profile_picture')
        address = request.POST.get('address')
        city = request.POST.get('city')  
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')

        user_check = User.objects.filter(username=email)

        if len(user_check) == 0:
            if password == confirm_password:  
                usr = User.objects.create_user(username=name, email=email, password=password)
                usr.first_name = name
                usr.save()

                profile = UserProfile.objects.create(
                    username=usr.username,
                    profile_picture=profile_picture,
                    email=email,
                    address=address,
                    city=city,
                    state=state,
                    pincode=pincode
                )

                context['status'] = f"User {name} Registered Successfully!"
            else:
                context['error'] = "Passwords do not match"
        else:
            context['error'] = "A User with this email already exists"

    return render(request, 'signup.html', context)

def login_user(request):
    context = {}

    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(username=name, password=password)
        if user:
            login(request, user)
            context['status'] = "Logged in successfully!"
            return redirect('dashboard')  # Redirect to dashboard
        else:
            context['error'] = "Invalid email or password"

    return render(request, 'login.html', context)

def dashboard(request):
    user = UserProfile.objects.get(username=request.user.username)
    context = {'user': user }
    return render(request, 'dashboard.html', context)
