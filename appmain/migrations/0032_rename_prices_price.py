# Generated by Django 5.1.4 on 2025-02-21 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0031_prices_alter_texastrip_package'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prices',
            new_name='Price',
        ),
    ]
