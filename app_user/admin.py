from django.contrib import admin
from .models import School, Relative, Student


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'region', 'district', 'city', 'school']


@admin.register(Relative)
class RelativeAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'patronymic', 'phone_number', 'email']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'parent', 'user_class', 'last_name', 'first_name', 'patronymic', 'phone_number']
