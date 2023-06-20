from django.urls import path

from restaurant.views import (
    RestaurantCreateView,
    RestaurantRetrieveView,
    RestaurantUpdateView,
)

app_name = "restaurant"

urlpatterns = [
    path('create/', RestaurantCreateView.as_view(), name='create-restaurant'),
    path('info/', RestaurantRetrieveView.as_view(), name='restaurant-info'),
    path('update/', RestaurantUpdateView.as_view(), name='restaurant-update'),
]
