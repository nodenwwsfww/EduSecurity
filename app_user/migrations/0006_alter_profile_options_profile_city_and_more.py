# Generated by Django 4.0.4 on 2022-06-26 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0005_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'главный родитель', 'verbose_name_plural': 'главный родитель'},
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Краснодар', max_length=50, verbose_name='Город (уч. заведения)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='patronymic',
            field=models.CharField(blank=True, max_length=25, verbose_name='Отчество'),
        ),
    ]
