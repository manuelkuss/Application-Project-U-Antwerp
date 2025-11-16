from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Sequence, MgfFile
from .models import Note

admin.site.register(Sequence)
admin.site.register(Note)
admin.site.register(MgfFile)