from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account's been created for {username}")
            return redirect('user-home')
    else:
        form = UserCreationForm()

    return render(request, "users/register.html", {"form": form})


def home(request):
    return render(request, 'user-home.html')
