from django import forms 
from .models import Review

class RestaurantReviewForm(forms.ModelForm):
    class Meta:
        model = Review 
        fields = ['rating', 'description','restaurant']
        
        
class FoodReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'description','food']
    