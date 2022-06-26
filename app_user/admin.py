from django.contrib import admin
from .models import School, Relative, Student, Profile


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    """Регистрация модели школы в админке"""
    list_display = ['id', 'region', 'district', 'city', 'school']


@admin.register(Relative)
class RelativeAdmin(admin.ModelAdmin):
    """Регистрация модели довереного лица в админке"""
    list_display = ['id', 'last_name', 'first_name', 'patronymic', 'phone_number', 'email']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Регистрация модели ученика в админке"""
    list_display = ['id', 'school', 'parent', 'user_class', 'last_name', 'first_name', 'patronymic', 'phone_number']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Регистрация модели профиля главного родителя в админке"""
    list_display = ['user', 'last_name', 'first_name', 'patronymic', 'phone_number', 'email', 'relative_type']
