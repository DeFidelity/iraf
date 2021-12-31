from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (RestaurantListView,RestaurantView,
                    FoodListView,FoodDetailView,)


urlpatterns = [
    path('restaurants/',RestaurantListView.as_view(),name="restaurants"),
    path('restaurant/<int:pk>/',RestaurantView.as_view(),name="restaurant"),
    path('foods/',FoodListView.as_view(),name='foods'),
    path('food/<int:pk>/',FoodDetailView.as_view(),name='food'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
