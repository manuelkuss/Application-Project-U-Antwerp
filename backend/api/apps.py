import os

from django.apps import AppConfig
from django.conf import settings
from django.core.management import call_command
from django.db import OperationalError
from django.db.models.signals import post_migrate

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        db_path = settings.DATABASES['default'].get('NAME')

        if db_path and not os.path.exists(db_path):
            post_migrate.connect(load_initial_data, sender=self)

            print("Database file not found. Creating DB...")
            try:
                call_command('makemigrations', interactive=False)
                call_command('migrate', interactive=False)

            except OperationalError as e:
                print("Migration error:", e)

def load_initial_data(sender, **kwargs):
    try:
        call_command('loaddata', settings.DATABASES['default'].get('FIXTURES_PATH'))
    except Exception as e:
        print("Error while inserting intitial data:", e)
