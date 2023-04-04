# stopwatch_timer
Write a stopwatch_timer with python web framework Django.

## Setting Up

* Writting Python codes with ChatGPT and others.

```shell
#src: https://docs.djangoproject.com/en/4.2/intro/tutorial01/#creating-a-project
django-admin startproject mytimer
cd mytimer
#src: https://docs.djangoproject.com/en/4.2/intro/tutorial01/#creating-the-polls-app
python manage.py startapp timer
```

## Deploy and test

```shell
#Show
tree . -d
################
.
├── mytimer
└── timer
    ├── migrations
    └── templates
#################
```

```shell
#Route Rules setting
cd timer
#first view
#src: https://docs.djangoproject.com/en/4.2/intro/tutorial01/#write-your-first-view
touch views.py
vim views.py
#src: create a URLconf
touch urls.py
vim urls.py

#point the root URLconf at the polls.urls module
#django.urls.include
#src: https://docs.djangoproject.com/en/4.2/ref/urls/#django.urls.include
#urlpatterns 
cd mytimer
vim mytimer/urls.py

python manage.py migrate
python manage.py runserver

#Check ULR
http://127.0.0.1:8000/timer/
```