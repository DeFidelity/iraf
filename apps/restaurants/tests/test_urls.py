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
        
    def test_food_try_urls(self):
        food_try = reverse('food-try',args=[2])
        
        response = resolve(food_try)
        
        self.assertEquals(response.func.view_class,FoodTryIt)
        
    def test_restaurant_like_urls(self):
        like = reverse('restaurant-like',args=['this-restaurant'])
        
        response = resolve(like)
        
        self.assertEquals(response.func.view_class,RestaurantLike)
        
    def test_restaurant_review_urls(self):
        reviews = reverse('restaurant-review',args=['this-restaurant'])
        
        response = resolve(reviews)
        
        self.assertEquals(response.func.view_class,RestaurantReview)
        
    def test_restaurant_review_delete(self):
        review_delete = reverse('review-delete',args=[3])
        
        response = resolve(review_delete)
        
        self.assertEquals(response.func.view_class,ReviewDelete)
        