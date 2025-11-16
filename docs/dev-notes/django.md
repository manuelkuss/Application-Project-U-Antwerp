django-admin startproject visualizeDataProject
cd visualizeDataProject
python manage.py startapp api
pip install djangorestframework
python manage.py makemigrations
python manage.py migrate
pip install django-cors-headers

Create superuser:
python manage.py createsuperuser
- Username: admin
- Password: admin

To run the server:
python manage.py runserver

 pip install "altair[all]" 