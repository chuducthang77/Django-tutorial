django-admin startproject mysite . 

python manage.py migrate 

python manage.py runserver 0.0.0.0:8000

python manage.py createsuperuser

python manage.py startapp feed
    - Create models in models.py 
    - Make the db editable in admin.py

python manage.py makemigrations