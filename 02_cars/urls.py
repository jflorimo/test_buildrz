from django.urls import path

from . import api


# Car
car_list = api.CarViewSet.as_view({"get": "list", "post": "create"})
car_detail = api.CarViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)

urlpatterns = [
    path("cars/", car_list, name="car-list"),
    path("cars/<int:pk>/", car_detail, name="car-detail"),
]
