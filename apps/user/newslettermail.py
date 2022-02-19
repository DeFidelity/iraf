from apps.blog.models import BlogPage
from datetime import date, timedelta

def send_weekly_mail():
    start_date = date.today()
    first_date = start_date + timedelta(days=7)
    blogs = BlogPage.objects.filter(date__range=(start_date, first_date))
    print(blogs)
# mail.send(
#     'adeyemihaki@gmail.com', # List of email addresses also accepted
#     'heedngrow@gmail.com',
#     subject='My email',
#     message='Hi there!',
#     html_message='Hi <strong>there</strong>!',
# )