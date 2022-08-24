"""
my_car_manager URL Configuration
"""

from django.urls import path

from .views import (
    RefuelingListView,
    RefuelingCreateView,
    RefuelingUpdateView,
    RefuelingDeleteView,
    RefuelingListViewFilterByCar
)

urlpatterns = [
    path("", RefuelingListView.as_view(), name="all-refuelings"),
    path(
        "new/<int:pk>/",
        RefuelingCreateView.as_view(),
        name="new-refueling"
    ),
    path(
        "update/<int:pk>/",
        RefuelingUpdateView.as_view(),
        name="refueling-update"
    ),
    path("delete/<int:pk>/",
         RefuelingDeleteView.as_view(),
         name="refueling-delete"
         ),
    path("car/<int:pk>",
         RefuelingListViewFilterByCar.as_view(),
         name="refueling-by-car"
         ),

]
