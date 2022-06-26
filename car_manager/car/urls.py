from django.urls import path
from car.views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
    path("", CarListView.as_view(), name="cars_home"),
    path("new-car/", CarCreateView.as_view(), name="add_car"),
    path("edit-car/<int:pk>", CarUpdateView.as_view(), name="edit_car"),
    path("detail-car/<int:pk>/", CarDetailView.as_view(), name="detail_car"),
    path("delete-car/<int:pk>/", CarDeleteView.as_view(), name="delete_car"),
]
