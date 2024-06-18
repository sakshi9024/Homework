from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name","email","age","address","phone_no","date"] 

# Register your models here.
