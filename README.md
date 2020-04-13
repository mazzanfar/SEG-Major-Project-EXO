# majorProjectEXO
To install:
1. To make sure you can use the project, have the latest version of python installed.
2. Using mac, brew install python:
a. In terminal: sudo easy_install pip



For installing postgreSQL on local machine: https://djangocentral.com/using-postgresql-with-django/


To run the project (make sure to be in the right directory):
1. Install libraries: pip install -r requirements.txt (if pip doesn't work use pip3)
2. Apply the migrations: python manage.py makemigrations, python manage.py migrate
3. Run: python manage.py runserver

To create a superuser(needed to access web crawler and database):
1. Add /admin to view database and admin login to the website returned
2. Add /health_data to view the web crawler

1.	web => To create a django project we use: django-admin.py startproject project_name
2.	To run the project: python3 manage.py runserver
3.	app => To make an app we use the command: python3 manage.py startapp app_name

Sources:
https://dev.to/coderasha/create-advanced-user-sign-up-view-in-django-step-by-step-k9m
https://www.stackoverflow.com
https://www.youtube.com/watch?v=Zx09vcYq1oc&list=PLLxk3TkuAYnpm24Ma1XenNeq1oxxRcYFT

Have coverage installed:
pip install coverage

Run test suite with coverage:
coverage erase  # ensure previous reports are removed
coverage run manage.py test
coverage report 