from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

      
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    like = models.ManyToManyField(User,related_name='+',blank=True)
    description = models.TextField(blank=True,null=True)
    location = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    contact = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    review = models.FloatField(default=0.0,null=True,blank=True)
    num_reviews = models.IntegerField(default=0)
    image = models.ImageField(verbose_name="restaurant_image", upload_to='media/restaurants/', default=None,null=True,blank=True,height_field=None, width_field=None)
    
    def perform_review(self,user,review,restaurant):
        has_reviewed = Review.objects.filter(review_user=user,restaurant=restaurant)
        if not has_reviewed:
            review = Review.objects.create(rating=review['rating'],description=review['description'],restaurant=restaurant)
            review.review_user = user
            if review.review_user:
                review.save()
            return None
        else:
            return None
        
    def __str__(self):
        return self.name
        
class FoodCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class Food(models.Model):
    name = models.CharField(max_length=255,unique=False)
    image = models.ImageField(verbose_name="food_image", upload_to='media/foods/', default=None,null=True,blank=True,height_field=None, width_field=None)
    restaurant = models.ForeignKey(Restaurant,related_name='restaurants',null=True,on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    description = models.TextField(null=True, blank=True)
    discount_price = models.PositiveSmallIntegerField()
    categories = models.ManyToManyField(FoodCategory, related_name='category',blank=True)
    star = models.FloatField(default=0.0,null=True, blank=True)
    try_it = models.ManyToManyField(User, related_name='try_it',blank=True)
    purchase = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['-date']
        
        
    def __str__(self):
        return self.name
    
    
    def has_purchased(self):
        return self.purchase + 1
    
    
class Review(models.Model):
    review_user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200,null=True)
    active = models.BooleanField(default=True)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name="restaurantreview",null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['rating',]
    
    def __str__(self):
        return f"{self.review_user} review for {self.restaurant}"
  

    