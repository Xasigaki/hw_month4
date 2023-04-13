# Generated by Django 4.2 on 2023-04-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название телефона')),
                ('description', models.TextField(blank=True, verbose_name='Описание телефона')),
                ('image', models.ImageField(upload_to='', verbose_name='фото:')),
                ('video', models.URLField(verbose_name='Видео')),
                ('cost', models.PositiveIntegerField(verbose_name='Стоимость в $')),
                ('model_phone', models.CharField(choices=[('Простые', 'Простые'), ('Бюджетные', 'Бюджетные'), ('Высокого класса', 'Высокого класса'), ('Премиум класса', 'Премиум класса'), ('Элитные', 'Элитные')], max_length=100, verbose_name='Модель телефонов')),
                ('сreated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]