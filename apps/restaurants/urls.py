from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (RestaurantListView,RestaurantDetailView,
                    FoodListView,FoodDetailView,RestaurantReview,
                    FoodTryIt,RestaurantLike, ReviewDelete)


urlpatterns = [
    path('',RestaurantListView.as_view(),name="restaurants"),
    path('restaurant/<slug:slug>/',RestaurantDetailView.as_view(),name="restaurant_detail"),
    path('foods/',FoodListView.as_view(),name='foods'),
    path('food/<str:restaurant>/food/<str:name>/',FoodDetailView.as_view(),name='food'),
    path('food/try-it/<int:pk>/',FoodTryIt.as_view(),name='food-try'),
    path('restaurant/like/<slug:slug>/',RestaurantLike.as_view(),name='restaurant-like'),
    path('restaurant/<slug:slug>/review',RestaurantReview.as_view(),name='restaurant-review'),
    path('restaurant/reviews/<int:pk>/delete/',ReviewDelete.as_view(),name='review-delete'),    
] 