from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (RestaurantListView,RestaurantDetailView,
                    FoodListView,FoodDetailView,)


urlpatterns = [
    path('',RestaurantListView.as_view(),name="restaurants"),
    path('restaurant/<int:pk>/',RestaurantDetailView.as_view(),name="restaurant_detail"),
    path('foods/',FoodListView.as_view(),name='foods'),
    path('food/<int:pk>/',FoodDetailView.as_view(),name='food'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
