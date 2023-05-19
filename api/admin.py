from django.contrib import admin
from .models import Job


@admin.register(Job)
class Job(admin.ModelAdmin):
    list_display = ['id', 'start_time', 'end_time']

"""
@admin.register(Step)
class Step(admin.ModelAdmin):
    list_display = ['id']
"""