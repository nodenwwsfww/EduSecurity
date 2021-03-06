from django.contrib.auth.models import User
from django.db import models


class School(models.Model):
    """Описание модели школы"""

    region = models.CharField(max_length=100, verbose_name='Регион')
    district = models.CharField(max_length=100, verbose_name='Городской округ/Муниципальный район')
    city = models.CharField(max_length=100, verbose_name='Населённый пункт')
    school = models.CharField(max_length=150, verbose_name='Образовательное учреждение')

    def __str__(self):
        return self.school

    class Meta:
        verbose_name_plural = 'школы'
        verbose_name = 'школа'


class Relative(models.Model):
    """Описание модели довереного лица"""

    main_parent = models.ForeignKey(User, default=1, on_delete=models.CASCADE, verbose_name='Главный родитель')
    last_name = models.CharField(max_length=25, verbose_name='Фамилия')
    first_name = models.CharField(max_length=25, verbose_name='Имя')
    patronymic = models.CharField(max_length=25, verbose_name='Отчество')
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')
    relative_type = models.CharField(max_length=15, blank=True, verbose_name='Степень родства')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name_plural = 'доверенные лица'
        verbose_name = 'доверенное лицо'


class Student(models.Model):
    """Описание модели ученика"""

    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='Школа')
    parent = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Родитель')
    user_class = models.CharField(max_length=3, verbose_name='Класс')
    last_name = models.CharField(max_length=25, verbose_name='Фамилия')
    first_name = models.CharField(max_length=25, verbose_name='Имя')
    patronymic = models.CharField(max_length=25, verbose_name='Отчество')
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name_plural = 'ученики'
        verbose_name = 'ученик'


class Profile(models.Model):
    """Описание модели профиля главного пользователя (родителя)"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    last_name = models.CharField(max_length=25, blank=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=25, blank=True, verbose_name='Имя')
    city = models.CharField(max_length=50, default='Краснодар', verbose_name='Город (уч. заведения)')
    patronymic = models.CharField(max_length=25, blank=True, verbose_name='Отчество')
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')
    relative_type = models.CharField(max_length=15, blank=True, verbose_name='Степень родства')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name_plural = 'главный родитель'
        verbose_name = 'главный родитель'
