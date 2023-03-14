from django.contrib import admin
from .models import *

class name(admin.ModelAdmin):
    list_display = ['name']
    
admin.site.register(Table,name)
