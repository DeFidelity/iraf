from django.contrib.sitemaps import Sitemap

from .models import Restaurant, Food

class RestaurantSitemap(Sitemap):
		changefreq = "weekly"
		priority = 0.9
		
		def items(self):
				return Restaurant.objects.all()
		
		def lastmod(self, obj):
				return obj.updated

class FoodSitemap(Sitemap):
		changefreq = "weekly"
		priority = 0.8
		
		def items(self):
				return Food.objects.all()
		
		def lastmod(self, obj):
				return obj.updated