from django.urls import path

from . import views

urlpatterns = [
    path("", views.CarListView.as_view(), name="cars-list"),
    path("new/", views.CarCreateView.as_view(), name="car-add"),
    path("edit-car/<int:pk>", views.CarUpdateView.as_view(), name="edit-car"),
    path(
        "detail-car/<int:pk>/",
        views.CarDetailView.as_view(),
        name="detail-car"),
    path("<int:pk>/delete", views.CarDeleteView.as_view(), name="car-delete"),
]
