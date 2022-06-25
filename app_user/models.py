from django.contrib.auth.models import User
from django.db import models


class School(models.Model):
    region = models.CharField(max_length=100, verbose_name='Регион')
    district = models.CharField(max_length=100, verbose_name='Городской округ/Муниципальный район')
    city = models.CharField(max_length=100, verbose_name='Населённый пункт')
    school = models.CharField(max_length=150, verbose_name='Образовательное учреждение')

    def __str__(self):
        return self.school


class Relative(models.Model):
    last_name = models.CharField(max_length=25, verbose_name='Фамилия')
    first_name = models.CharField(max_length=25, verbose_name='Имя')
    patronymic = models.CharField(max_length=25, verbose_name='Отчество')
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='Школа')
    parent = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Родитель')
    user_class = models.CharField(max_length=3, verbose_name='Класс')
    last_name = models.CharField(max_length=25, verbose_name='Фамилия')
    first_name = models.CharField(max_length=25, verbose_name='Имя')
    patronymic = models.CharField(max_length=25, verbose_name='Отчество')
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона')
