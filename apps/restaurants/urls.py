from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (RestaurantListView,RestaurantDetailView,
                    FoodListView,FoodDetailView,RestaurantReview,
                    FoodTryIt,RestaurantLike, ReviewDelete)


urlpatterns = [
    path('',RestaurantListView.as_view(),name="restaurants"),
    path('restaurant/<int:pk>/',RestaurantDetailView.as_view(),name="restaurant_detail"),
    path('foods/',FoodListView.as_view(),name='foods'),
    path('food/<int:pk>/',FoodDetailView.as_view(),name='food'),
    path('food/try-it/<int:pk>/',FoodTryIt.as_view(),name='food-try'),
    path('restaurant/like/<int:pk>/',RestaurantLike.as_view(),name='restaurant-like'),
    path('restaurant/<int:pk>/review',RestaurantReview.as_view(),name='restaurant-review'),
    path('restaurant/reviews/<int:pk>/delete/',ReviewDelete.as_view(),name='review-delete'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
