# Generated by Django 5.1.4 on 2025-01-11 01:47

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0016_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
