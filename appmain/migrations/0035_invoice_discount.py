# Generated by Django 5.1.4 on 2025-02-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0034_alter_price_is_obsolete_alter_price_second_tax_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='discount',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
