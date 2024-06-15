from django.contrib import admin

# Register your models here.
from .models import Note,Entry

admin.site.register(Note)
admin.site.register(Entry)