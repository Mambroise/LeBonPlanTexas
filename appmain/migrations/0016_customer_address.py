# Generated by Django 5.1.4 on 2025-01-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0015_rename_price_driver_invoice_driver_price_excl_tax_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Adresse'),
        ),
    ]
