from django.contrib import admin
from .models import Job, Step



@admin.register(Job)
class Job(admin.ModelAdmin):
    list_display = ['id', 'start_time', 'end_time'] 
