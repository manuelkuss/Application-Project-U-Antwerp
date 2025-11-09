django-admin startproject visualizeDataProject
cd visualizeDataProject
python manage.py startapp api
pip install djangorestframework
python manage.py makemigrations
python manage.py migrate
pip install django-cors-headers


To run the server:
python manage.py runserver

