# Generated by Django 5.1.3 on 2024-11-20 05:42

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(default='любое место', max_length=100, verbose_name='Место выполнения')),
                ('date', models.DateField(verbose_name='Время выполнения')),
                ('action', models.CharField(max_length=100, verbose_name='Действие')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='Приятная привычка')),
                ('period', models.CharField(choices=[('ONE', 'один'), ('TWO', 'два'), ('THREE', 'три'), ('FOUR', 'четыре'), ('FIVE', 'пять'), ('SIX', 'шесть'), ('SEVEN', 'семь')], default='ONE', max_length=20, verbose_name='периодичность')),
                ('reward', models.CharField(blank=True, max_length=100, null=True, verbose_name='Награда')),
                ('time_required', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(120)], verbose_name='Необходимое время выполнения, сек.')),
                ('is_public', models.BooleanField(default=False, verbose_name='Публичность')),
                ('connected', models.ManyToManyField(blank=True, null=True, to='habits.habit')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор привычки')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
                'ordering': ['-date'],
            },
        ),
    ]