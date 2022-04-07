from ast import arg
from django.test import TestCase, Client
from django.urls import reverse 
from django.contrib.auth.models import User
from apps.restaurants.models import Restaurant, FoodCategory, Food, Review


class TestRestaurantViewClasses(TestCase):
    
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
        
    def test_restaurant_list_view(self):
        restaurant_list = reverse('restaurants')
        
        response = self.client.get(restaurant_list)
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('restaurant/restaurant-list.html')
        
    def test_restaurant_detail_view(self):
        restaurant = reverse('restaurant_detail',args=[self.restaurant.slug])
        response = self.client.get(restaurant)
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('restaurant/restaurant.html')
        
    def test_food_list_view(self):
        food = reverse('foods')
        
        response = self.client.get(food)
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('restaurant/food-list.html')
        
    def test_food_detail_view(self):
        food = reverse('food',kwargs={'restaurant':self.restaurant.pk,'name':self.food.name})
        
        response = self.client.get(food)
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('restaurant/food-detail.html')
        
    def test_restaurant_review_with_anon_user(self):
        review = reverse('restaurant-review',args=[self.restaurant.slug])
        
        response = self.client.post(review,data={
            'review_user': self.user,
            
            'rating': 4,
            'description': 'i ate there and it was great'
        })
        
        
        self.assertEquals(response.status_code,302)
        self.assertTemplateUsed('restaurant/restaurant.html')
        
    def test_restaurant_review_with_logged_in_user(self):
        review = reverse('restaurant-review',args=[self.restaurant.slug])
        
        self.client.login(email=self.user.email,password = 'testpassword')
        response = self.client.post(review,data={
            'review_user': self.user,
            
            'rating': 4,
            'description': 'i ate there and it was great'
        })
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('restaurant/restaurant.html')
        
    def test_food_try_it_with_anon_user(self):
        food_try = reverse('food-try',args=[self.food.pk])
        
        response = self.client.post(food_try)
        
        self.assertEquals(response.status_code,302)
        
    def test_food_try_it_with_logged_in_user(self):
        food_try = reverse('food-try',args=[self.food.pk])
        
        self.client.login(email=self.user.email,password = 'testpassword')
        response = self.client.post(food_try)
        
        self.assertEquals(response.status_code,200)
        
    def test_restaurant_like_with_guest_user(self):
        like = reverse('restaurant-like', args=[self.restaurant.pk])
        
        response = self.client.post(like)
        
        self.assertEquals(response.status_code,302)
        
    def test_restaurant_like_with_logged_in_user(self):
        like = reverse('restaurant-like', args=[self.restaurant.pk])
        
        self.client.login(email=self.user.email,password = 'testpassword')
        response = self.client.post(like)
        
        self.assertEquals(response.status_code,200)

    def test_review_delete_with_no_user(self):
        delete = reverse('review-delete', args=[self.review.pk])
        
        response = self.client.post(delete)
        
        self.assertEquals(response.status_code,302) 
        
    def test_review_delete_with_logged_in_user(self):
        delete = reverse('review-delete', args=[self.review.pk])
        
        self.client.login(email=self.user.email,password = 'testpassword')
        response = self.client.post(delete)
        
        
        self.assertEquals(response.status_code,302) 
           