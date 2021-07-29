from django.contrib import admin
from .models import Project, Assignment, Reminder

admin.site.register(Project)
admin.site.register(Assignment)
admin.site.register(Reminder)