# Generated by Django 3.1.6 on 2021-05-29 11:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eaptekahack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatmentcourse',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный курс?'),
        ),
        migrations.AddField(
            model_name='treatmentcourse',
            name='is_enabled_for_generation',
            field=models.BooleanField(default=True, verbose_name='Генерировать события?'),
        ),
        migrations.AddField(
            model_name='treatmentcourse',
            name='number_of_events',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество событий приема'),
        ),
        migrations.CreateModel(
            name='MedicationReminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planned_datetime', models.DateTimeField(verbose_name='Дата и время события')),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='reminder',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Юзер',
                    ),
                ),
            ],
        ),
    ]
