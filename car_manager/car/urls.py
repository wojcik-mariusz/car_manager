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
from django.urls import path
from car.views import home, add_new_car, edit_car, CarListView

urlpatterns = [
    path("", CarListView.as_view(), name="cars_home"),
    path("new-car/", add_new_car, name="add_car"),
    path("edit-car/<int:id>", edit_car, name="edit_car"),
]
