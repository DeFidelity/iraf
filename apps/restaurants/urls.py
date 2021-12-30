from django.urls import path
from .views import (RestaurantListView,RestaurantView,
                    FoodListView,FoodDetailView,)
urlpatterns = [
    path('restaurants/',RestaurantListView.as_view(),name="restaurants"),
    path('restaurant/<int:pk>/',RestaurantView.as_view(),name="restaurant"),
    path('foods/',FoodListView.as_view(),name='foods'),
    path('food/<int:pk>/',FoodDetailView.as_view(),name='food'),
]
