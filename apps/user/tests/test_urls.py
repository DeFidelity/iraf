from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.user.views import ProfileView, ProfileEdit, NewsletterView, ContactView


class TestUrls(SimpleTestCase):
    
    def test_profile_url(self):
        profile = reverse('profile')
        
        response = resolve(profile)
        
        self.assertEquals(response.func.view_class,ProfileView)
        
    def test_profile_edit_url(self):
        profile = reverse('profile-edit')
        
        response = resolve(profile)
        
        self.assertEquals(response.func.view_class,ProfileEdit)
        
    def test_newsletter_url(self):
        newsletter = reverse('newsletter')
        
        response = resolve(newsletter)
        
        self.assertEquals(response.func.view_class,NewsletterView)
        
        
    def test_contact_url(self):
        contact = reverse('contact')
        
        response = resolve(contact)
        
        self.assertEquals(response.func.view_class,ContactView)
        
    
        