from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import User


# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            messages.success(request, "User Registered Successfully!")

            login(request, user)
            return redirect('user_home')

    else:
        form = UserRegistrationForm()
    return render(request, "signup.html", {'form': form})


def signin(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in!")
        return redirect("index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get('password')

        try:
            User.objects.get(email=email)
        except:
            messages.warning(request, f"User does not exist. Create a new account")
            return redirect("signin")

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("home")

        else:
            messages.warning(request, "Password Incorrect!")
            return redirect("signin")


    else:
        return render(request, "signin.html")


def signout(request):
    logout(request)
    messages.success(request,"Logged out Successfully!")
    return redirect("index")
