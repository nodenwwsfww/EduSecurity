# Generated by Django 4.0.4 on 2022-06-26 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100, verbose_name='Регион')),
                ('district', models.CharField(max_length=100, verbose_name='Городской округ/Муниципальный район')),
                ('city', models.CharField(max_length=100, verbose_name='Населённый пункт')),
                ('school', models.CharField(max_length=150, verbose_name='Образовательное учреждение')),
            ],
            options={
                'verbose_name': 'школа',
                'verbose_name_plural': 'школы',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_class', models.CharField(max_length=3, verbose_name='Класс')),
                ('last_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=25, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=25, verbose_name='Отчество')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Родитель')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_user.school', verbose_name='Школа')),
            ],
            options={
                'verbose_name': 'ученик',
                'verbose_name_plural': 'ученики',
            },
        ),
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=25, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=25, verbose_name='Отчество')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('relative_type', models.CharField(blank=True, max_length=15, verbose_name='Степень родства')),
                ('main_parent', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Главный родитель')),
            ],
            options={
                'verbose_name': 'доверенное лицо',
                'verbose_name_plural': 'доверенные лица',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=25, verbose_name='Фамилия')),
                ('first_name', models.CharField(blank=True, max_length=25, verbose_name='Имя')),
                ('city', models.CharField(default='Краснодар', max_length=50, verbose_name='Город (уч. заведения)')),
                ('patronymic', models.CharField(blank=True, max_length=25, verbose_name='Отчество')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('relative_type', models.CharField(blank=True, max_length=15, verbose_name='Степень родства')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'главный родитель',
                'verbose_name_plural': 'главный родитель',
            },
        ),
    ]