# majorProjectEXO

Needed for postgreSQL:
pip install psycopg2

pip install pillow

pip install django-crispy-forms

For installing postgreSQL on local machine: https://djangocentral.com/using-postgresql-with-django/


1.	web => To create a django project we use: django-admin.py startproject project_name
2.	To run the project: python3 manage.py runserver
3.	app => To make an app we use the command: python3 manage.py startapp app_name

To run the project:
1. Install libraries: pip install -r requirements.txt
2. Apply the migrations: python manage.py migrate
3. Run: python manage.py runserver


Sources:
https://dev.to/coderasha/create-advanced-user-sign-up-view-in-django-step-by-step-k9m

Have coverage installed:
pip install coverage

Run test suite with coverage:
coverage erase  # ensure previous reports are removed
coverage run manage.py test
coverage report 