from django.contrib import admin
from .models import MgfFile
from .models import Note

# Register your models here.

admin.site.register(Note)
admin.site.register(MgfFile)