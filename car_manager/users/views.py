from django.shortcuts import render, redirect
from users.forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username: str = form.cleaned_data.get('username')
            messages.success(request, f"Account's been created for {username}")
            form.save()
            return redirect('user-home')
    else:
        form = UserRegistrationForm()

    return render(request, "users/register.html", {"form": form})


def home(request):
    return render(request, 'user-home.html')
