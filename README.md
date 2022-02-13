# iraf

food delivery, restaurant rating and blogging app.


## Description and Inspiration

This project was inspired by a friend when I was stranded and need to build some representative webapps for my portfolio, describing her idea she stated it'll be nice to have a food blog but with inclusion of user registration and authorization, from it users can also see list of popular restaurants and their menu. Then registered users would be allow to rate the restaurants they've been to while to the app would later be used to order foods from top restaurants.


## Language, Framework and Libraries 
This are the list of Framework and Libraries used in bringing this project to live, thanks to HTMX it wouldn't have been this sleeky without it.
- Python
- Django
- HTML
- HTMX
- Tailwind CSS
- Alpine JS




## Installation Guide

Before you'll be able to run this project, you must have python installed with pip or pip 3 enabled.
Clone the repository and run
`pip install -r requirements.txt` 
This command would install all the project requirements on your machine, I'll suggest you do all this in a virtual environment.
After dependency installations run `python manage.py make migrations` and `python manage.py migrate` which would migrate everything in this projects migration folder to an SQLite db.
The project should be ready by now, so run `pytjon manage.py runserver`, navigate to your browser and follow the prescribed local host url. You should see this project in its full glory.

## Usability

This project can be used for primarily any of the afforementioned user query except for ordering food from restaurants, it's not done just because we need the restaurants permission to use crawl their site and I can't really afford to contact them one after the other.

## Credits

While on the course of this project I used allot of existing packages to get things done easily and the list are:

- Django Allauth (for authentication and social auth)
- Jazzmin (for bootstrap admin template)
- Wagtail (used as CMS for blog side of the project)
- Django Tailwind ( to use tailwind jit mode )

# Goals

This project contribute significantly to my career as an aspiring Software Engineer, strengthen me in solving my own problems and pushes me to learn more things whenever a new features cracks my head, what I noticed after this project is that I feel comfortable doing my thing and I feel I'm competent anough to embark on a journey to use my skill to polish technology as much as I can.


