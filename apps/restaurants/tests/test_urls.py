from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from apps.restaurants.views import (RestaurantListView,RestaurantDetailView,
                            FoodListView,FoodDetailView,RestaurantReview,
                            FoodTryIt,RestaurantLike, ReviewDelete)


class TestUrls(SimpleTestCase):
    
    def test_restaurant_list_view_url(self):
        restaurants = reverse('restaurants')
        
        response = resolve(restaurants)
        
        self.assertEquals(response.func.view_class,RestaurantListView)
        
    def test_restaurant_details_url(self):
        restaurant = reverse('restaurant_detail',args=['this-restaurant'])
        
        response = resolve(restaurant)
        
        self.assertEquals(response.func.view_class,RestaurantDetailView)
        
    def test_food_list_urls(self):
        foods = reverse('foods')
        
        response = resolve(foods)
        
        self.assertEquals(response.func.view_class,FoodListView)
        
    def test_food_detail_urls(self):
        
        food = reverse('food',args=['restaurant','food-name'])
        
        response = resolve(food)
        
        self.assertEquals(response.func.view_class,FoodDetailView)
        