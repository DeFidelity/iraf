from django.db import models
from django.contrib.auth.models import User


class Rating(models.Model):
    user = models.ForeignKey(User,related_name='user_rating',on_delete=models.CASCADE)
    review = models.TextField(max_length=300)
    stars = models.PositiveSmallIntegerField()
    would_recomend = models.BooleanField(default=False)
        
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    contact = models.CharField(max_length=255)
    is_discounted = models.BooleanField(default=False)
    rating = models.ForeignKey(Rating,related_name='rating',null=True,blank=True,on_delete=models.CASCADE)
    
    

class Food(models.Model):
    name = models.CharField(max_length=255,unique=False)
    restaurants = models.ForeignKey(Restaurant,related_name='restaurants',null=True,on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    discount_price = models.PositiveSmallIntegerField()
    rating = models.ForeignKey(Rating,related_name='food_rating',null=True, blank=True,on_delete=models.CASCADE)
    purchase = models.IntegerField(default=0)
    
    def has_purchased(self):
        return self.purchase + 1
    

    