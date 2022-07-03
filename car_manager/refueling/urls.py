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

from .views import (
    RefuelingListView,
    RefuelingCreateView,
    RefuelingUpdateView,
    RefuelingDeleteView,
)

urlpatterns = [
    path("", RefuelingListView.as_view(), name="all-refuelings"),
    path("new/<int:pk>/", RefuelingCreateView.as_view(), name="new-refueling"),
    path("update/<int:pk>/", RefuelingUpdateView.as_view(), name="refueling-update"),
    path("delete/<int:pk>/", RefuelingDeleteView.as_view(), name="refueling-delete"),
]
