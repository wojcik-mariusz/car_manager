"""my_car_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from users import views as user_views
from car import views as car_views


urlpatterns = [
    path("", car_views.home, name="welcome=page"),
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("cars/", include("car.urls"), name="car-home"),
    path("register/", user_views.register, name="register"),
    path("register/home/", user_views.home, name="user-home"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path("profile/", user_views.profile, name="profile"),
    path(
        "change-password/",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/change_password.html",
        ),
        name="change_password",
    ),
    path(
        "password-change-done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="registration/password_change_done-confirm.html"
        ),
        name="password_change_done",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
    ),
    path(
        "password-reset-sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done_info.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm-form/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm_form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete-confirm/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete_confirm_info.html"
        ),
        name="password_reset_complete",
    ),
    path("rf/", include("refueling.urls"), name="refueling-home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
