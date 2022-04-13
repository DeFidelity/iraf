from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from apps.restaurants.models import Restaurant, FoodCategory, Food, Review 

class TestRestaurantModelMethods(TestCase):
    def setUp(self):
        self.client = Client()
        
        self.user = User.objects.create_user(
            username= 'user',
            email = 'reader@mail.com',
            password = 'testpassword'
        )
        
        self.restaurant = Restaurant.objects.create(
            name = 'Kilishi hub',
            description = 'we sell all types of assorted kilishi',
            location = 'Lagos',
            email ='kilishi@hub.com',
            contact = 'kilishi@mail.com',
            about = 'something about us',
        )
        
        self.food_category = FoodCategory.objects.create(
            name = 'meats',
            description = 'about processed meats',
        )
        
        self.food = Food.objects.create(
            name = 'yaji',
            restaurant = self.restaurant,
            price = 3000,
            description = 'kilisha sauce',
            discount_price = 2000
        )
        categ = FoodCategory.objects.all() 
        for food in categ:
            self.food.categories.add(food)
        
        self.review = Review.objects.create(
            review_user = self.user,
            rating = 4.5,
            description = 'it is a very solid restaurant, i enjoyed it',
            restaurant = self.restaurant,
        )
        
    def test_slugify_method_in_save(self):
        slug = self.restaurant.slug 
        
        self.assertEquals(slug,'kilishi-hub')
        
    def test_perform_review_method(self):
        
        response = self.restaurant.perform_review(user=self.user,review=5,restaurant=self.restaurant)
        
        # self.assertEquals(self.restaurant.rating,5.0)
        self.assertEquals(self.restaurant.reviews.count(),1)
            
    def test_get_absolute_url(self):
            detail = reverse('restaurant_detail',args=[self.restaurant.slug])
            
            self.assertEquals(self.restaurant.get_absolute_url,detail)
            
            
            