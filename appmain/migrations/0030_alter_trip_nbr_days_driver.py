# Generated by Django 5.1.4 on 2025-01-29 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0029_remove_trip_vehiculed_trip_nbr_days_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='nbr_days_driver',
            field=models.IntegerField(default=0, null=True, verbose_name='Nombre de jour de service'),
        ),
    ]
