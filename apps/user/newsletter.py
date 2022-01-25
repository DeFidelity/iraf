from .models import NewsLetter 

def add_to_newsletter(email):
    newsletter = NewsLetter.objects.get(email=email)
    if newsletter:
        return True 
    else:
        subscribe= NewsLetter.objects.create(email=email)
        subscribe.save()
        return True
        
def remove_from_newsletter(email):
    newsletter = NewsLetter.objects.get(email=email)
    if newsletter:
        newsletter.delete()
        return True 
    else:
        return True
    