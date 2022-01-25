from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.blog.models import BlogPage

class UserProfile(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    BINARY = 'binary'
    NILL = 'nill'

    CHOICES = [
        (MALE, 'male'),
        (FEMALE, 'female'),
        (BINARY, 'binary'),
        (NILL, 'nill')
    ]
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    username = models.CharField(max_length=25, blank=True, null=True)
    display_name = models.CharField(max_length=20,blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    additional_mail = models.EmailField(blank=True,null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    collections = models.ManyToManyField(BlogPage,related_name='collection',blank=True)
    gender = models.CharField(max_length=20,choices=CHOICES, blank=True, null=True)



class NewsLetter(models.Model):
    email = models.EmailField(max_length=100,unique=True)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100,blank=True)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.email)


from .newsletter import add_to_newsletter



@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()


