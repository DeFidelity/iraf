from django.test import TestCase
from .models import BlogPage 

class BlogTestCase(TestCase):
    def setUp(self):
        blogs = BlogPage.objects.all()
        
    def test_blog_list(self):
        blog = BlogPage.objects.get(pk=5)
        self.assertEqual(blog.title())
