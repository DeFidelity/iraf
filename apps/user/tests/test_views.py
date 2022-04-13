from django.test import TestCase, Client
from django.urls import reverse 
from django.contrib.auth.models import User
from apps.restaurants.models import Restaurant, FoodCategory, Food, Review



class TestUserViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        
        self.user = User.objects.create_user(
            username= 'user',
            email = 'reader@mail.com',
            password = 'testpassword'
        )
        
       
    def test_profile_view(self):
        profile = reverse('profile')
        
        self.client.login(email=self.user.email,password = 'testpassword')
        
        response = self.client.get(profile)
        
        self.assertEquals(response.status_code,200)
        self.assertTrue(response.context['profile'])
        
    def test_profile_edit_view(self):
        profile_edit = reverse('profile-edit')
        
        self.client.login(email=self.user.email,password = 'testpassword')
        
        response = self.client.get(profile_edit)
        
        self.assertEquals(response.status_code,200)
    
    def test_profile_edit_view_POST(self):
        profile_edit = reverse('profile-edit')
        
        self.client.login(email=self.user.email,password = 'testpassword')
        
        response = self.client.post(profile_edit,data={
            'username': 'test user',
            'phone_number': '32098404',
            'address': '23 this street, test all',
            'display_name': 'boss test'
        })
        
        self.assertEquals(response.status_code,302)
        
    def test_newsletter_view(self):
        news = reverse('newsletter')
        
        response = self.client.post(news,data={
            'email': 'test@mail.com'
        })
        
        self.assertEquals(response.status_code,200)
        
    def test_contact_view(self):
        contact = reverse('contact')
        
        response = self.client.get(contact)
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('contact.html')
        
    def test_contact_view_POST(self):
        contact = reverse('contact')
        
        response = self.client.post(contact,data={
            'name': 'Test',
            'email': 'test@mail.com',
            'message': 'testing your contact'
        })
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('contact.html')
        
    
        
        