from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username: str = form.cleaned_data.get("username")
            messages.success(request, f"Account's been created for {username}")
            form.save()
            return redirect("user-home")
    else:
        form = UserRegistrationForm()

    return render(request, "users/register.html", {"form": form})


def home(request):
    return render(request, "user-home.html")


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user
        )

        if all((user_form.is_valid(), profile_form.is_valid())):
            user_form.save()
            profile_form.save()
            messages.success(request, "Update success!")
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)

    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, "users/profile.html", context)
