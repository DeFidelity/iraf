from django.contrib.sitemaps import Sitemap

from .models import BlogPage, BlogCategory

class PostSitemap(Sitemap):
		changefreq = "weekly"
		priority = 0.9
		
		def items(self):
				return BlogPage.objects.all()
		
		def lastmod(self, obj):
				return obj.updated

class CategorySitemap(Sitemap):
		changefreq = "weekly"
		priority = 0.8
		
		def items(self):
				return BlogCategory.objects.all()
		
		def lastmod(self, obj):
				return obj.updated