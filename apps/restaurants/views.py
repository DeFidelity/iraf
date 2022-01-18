from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views import View 
from django.contrib import messages

from .models import Review, Restaurant, Food 
from .forms import RestaurantReviewForm


class RestaurantListView(View):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        
       
        context = {
            'restaurants': restaurants,
        }
        return render(request,'restaurant/restaurant-list.html', context)


class RestaurantDetailView(View):
    def get(self,request,pk,*args,**kwargs):
        restaurant = get_object_or_404(Restaurant,pk=pk)
        foods = Food.objects.filter(restaurant=restaurant)
        reviews = Review.objects.filter(restaurant=restaurant)
        paginator = Paginator(reviews,5)
        
        five = Review.objects.filter(restaurant=restaurant,rating=5)
        four = Review.objects.filter(restaurant=restaurant,rating=4)
        three = Review.objects.filter(restaurant=restaurant,rating=3)
        two = Review.objects.filter(restaurant=restaurant,rating=2)
        one = Review.objects.filter(restaurant=restaurant,rating=1)
            
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'restaurant':restaurant,
            'foods': foods,
            'reviews': reviews,
            'page_number':page_number,
            'page_obj':page_obj,
            'one': one,
            'two':two,
            'three':three,
            'four': four,
            'five':five
        }
        return render(request, 'restaurant/restaurant.html', context)
    


class FoodListView(View):
    def get(self, request):
        foods = Food.objects.all()
        paginator = Paginator(foods,20)
        
            
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
            
        context = {
            'foods':foods,
            'page_number': page_number,
            'page_obj': page_obj,
        }
        
        return render(request, 'restaurant/food-list.html',context)
    

class FoodDetailView(View):
    def get(self,request,pk):
        food = get_object_or_404(Food, pk=pk)
        categories = food.categories.all()
        
        context = {
            'categories': categories,
            'food': food,
        }   

        return render(request,'restaurant/food-detail.html',context)


class RestaurantReview(View,LoginRequiredMixin):
    def post(self,request,pk,*args,**kwargs):
        restaurant = get_object_or_404(Restaurant,pk=pk)
        food = Food.objects.filter(restaurant=restaurant)
        form = RestaurantReviewForm(request.POST)
        
        user = request.user
        review_check = Review.objects.filter(review_user=user,restaurant=restaurant)

        
        if review_check:
            return HttpResponse('You have review this restaurant before')
    
        if form.is_valid():
            restaurant.perform_review(user=request.user,review=form.cleaned_data,restaurant=restaurant)
            return HttpResponse("Your review has been committed")
        else:
            return HttpResponse('Form not valid')
    
    
class FoodTryIt(View,LoginRequiredMixin):  
    def post(self, request,pk,*args,**kwargs):
        food = get_object_or_404(Food, pk=pk)
        categories = food.categories.all()
        user = request.user
        if user in food.try_it.all():
            food.try_it.remove(user)
            return HttpResponse('removed')
        
        else:
            food.try_it.add(user)
            return HttpResponse('added')

    
class RestaurantLike(View):
    def post(self, request,pk,*args,**kwargs):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        user = request.user
        
        if user in restaurant.like.all():
            restaurant.like.remove(user)
            likes = len(restaurant.like.all())
            messages.success(request,likes)
            return HttpResponse('unliked')
        else:
            restaurant.like.add(user)
            likes = len(restaurant.like.all())
            messages.success(request,likes)
            return HttpResponse('Liked')