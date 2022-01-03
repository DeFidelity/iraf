from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views import View 


from .models import Review, Restaurant, Food 
from .forms import RestaurantReviewForm, FoodReviewForm


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
        
            
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'restaurant':restaurant,
            'foods': foods,
            'reviews': reviews,
            'page_number':page_number,
            'page_obj':page_obj,
        }
        return render(request, 'restaurant/restaurant.html', context)
    
    
    def post(self,request,pk,*args,**kwargs):
        restaurant = get_object_or_404(Restaurant,pk=pk)
        food = Food.objects.filter(restaurant=restaurant)
        form = RestaurantReviewForm(request.POST)
        
        if form.is_valid():
            form.save(commit=False)
            restaurant.perform_review(user=request.user,review=form.cleaned_data)
            form.save()
            return HttpResponse("Your review has been committed")
        else:
            
            context = {
                'restaurant':restaurant,
                'food': food,
                'error': 'there was an error processing your request'
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
    def get(self, request,pk):
        food = get_object_or_404(Food, pk=pk)
        categories = food.categories.all()
        review = Review.objects.filter(food=food)
        paginator = Paginator(review,5)
        
            
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'categories': categories,
            'food': food,
            'review': review,
            'page_number':page_number,
            'page_obj':page_obj,
        }   

        return render(request,'restaurant/food-detail.html',context)
    
    def post(self, request,pk,*args,**kwargs):
        food = get_object_or_404(Food, pk=pk)
        categories = food.categories.all()
        form = FoodReviewForm(request.POST)
        if form.is_valid():
            food.perform_review(user=request.user,review=form.cleaned_data)
            form.save()

            return HttpResponse("Review added")
        
        context = {
            'categories': categories,
            'food': food,
        } 
        return render(request,'restaurant/food-detail.html')
    