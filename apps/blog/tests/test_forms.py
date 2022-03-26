from django.test import SimpleTestCase 
from apps.blog.forms import CommentForm 

class TestForms(SimpleTestCase):
    
    def test_comment_form(self):
        
        form = CommentForm(
            data ={
                 'comment':'this is the comment'
            }
        )
        
        self.assertTrue(form.is_valid)