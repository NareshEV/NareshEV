from django.contrib import admin
from .models import student
from .models import staff
admin.site.register(student)
admin.site.register(staff)