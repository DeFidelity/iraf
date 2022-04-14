# iraf

A Glassdoor, but for restaurants.

Featuring food delivery, restaurant review and blogging app.

### Screenshot of the food listing page
![Screenshot 2022-01-12 082042](https://user-images.githubusercontent.com/68183305/154834182-3086045f-c96f-4151-9cba-9ce505a9f5f5.png)



## Description and Inspiration

This project was inspired by a friend when I was stranded and need to build some representative webapps for my portfolio, describing her idea she stated it'll be nice to have a food blog but with inclusion of user registration and authorization, from it users can also see list of popular restaurants and their menu. Then registered users would be allow to rate the restaurants they've been to while to the app would later be used to order foods from top restaurants.

### screenshot of the food detail page
![Screenshot 2022-01-13 020946](https://user-images.githubusercontent.com/68183305/154834380-b8f0ecdd-73b3-479a-8b17-70ebaf05527d.png)


## Language, Framework and Libraries 
This are the list of Framework and Libraries used in bringing this project to live, thanks to HTMX it wouldn't have been this sleeky without it.
- Python
- Django
- HTML
- HTMX
- Tailwind CSS
- Alpine JS

### Screenshot of blog list page
![Screenshot 2022-01-12 082844](https://user-images.githubusercontent.com/68183305/154834209-5802558c-edac-45f4-8ac5-579ff43858de.png)



## Installation Guide

Before you'll be able to run this project, you must have python installed with pip or pip 3 enabled.
Clone the repository and run
`pip install -r requirements.txt` 
This command would install all the project requirements on your machine, I'll suggest you do all this in a virtual environment.
After dependency installations run `python manage.py make migrations` and `python manage.py migrate` which would migrate everything in this projects migration folder to an SQLite db.



The project should be ready by now, so run `pytjon manage.py runserver`, navigate to your browser and follow the prescribed local host url. You should see this project in its full glory.

### Screenshot of restaurant detail wih their menu
![Screenshot 2022-01-15 125549](https://user-images.githubusercontent.com/68183305/154834243-7d426622-c38c-4261-a68f-447dd8bbf8d5.png)

## Usability

This project can be used for primarily any of the afforementioned user query except for ordering food from restaurants, it's not done just because we need the restaurants permission to use crawl their site and I can't really afford to contact them one after the other.


### screenshot of wagtail page for blog management
![Screenshot 2022-01-12 085445](https://user-images.githubusercontent.com/68183305/154834274-9d6755c6-934b-425a-9a69-470af95d0352.png)


## Credits

While on the course of this project I used allot of existing packages to get things done easily and the list are:

- Django Allauth (for authentication and social auth)
- Jazzmin (for bootstrap admin template)
- Wagtail (used as CMS for blog side of the project)
- Django Tailwind ( to use tailwind jit mode )

### Screenshot of comment section with reply box

![Screenshot 2022-01-12 083012 - Copy](https://user-images.githubusercontent.com/68183305/154834321-595ce531-8c2e-4d1e-9180-6fe7768bddf5.png)

# Goals

This project contribute significantly to my career as an aspiring Software Engineer, strengthen me in solving my own problems and pushes me to learn more things whenever a new features cracks my head, what I noticed after this project is that I feel comfortable doing my thing and I feel I'm competent anough to embark on a journey to use my skill to polish technology as much as I can.

### mobile view
![Screenshot 2022-01-13 030036](https://user-images.githubusercontent.com/68183305/154834341-6824d140-5e8a-442e-a447-af753a9ba5bb.png)
![Screenshot 2022-01-13 030430 - Copy](https://user-images.githubusercontent.com/68183305/154834357-6104a563-7c7f-4bfa-83f7-e9b6e7abf696.png)
![Screenshot 2022-01-12 083958](https://user-images.githubusercontent.com/68183305/154834439-4403c3a0-c07d-49ec-b91e-b357ff1625fd.png)

GitHub < cause why not? 


