from django.urls import path

from . import views

urlpatterns = [
    path("", views.CarListView.as_view(), name="cars_list"),
    path("new/", views.CarCreateView.as_view(), name="car_add"),
    path("edit-car/<int:pk>", views.CarUpdateView.as_view(), name="edit_car"),
    path("detail-car/<int:pk>/", views.CarDetailView.as_view(), name="detail_car"),
    path("<int:pk>/delete", views.CarDeleteView.as_view(), name="car-delete"),
]
