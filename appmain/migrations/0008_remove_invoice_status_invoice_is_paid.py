# Generated by Django 5.1.4 on 2025-01-04 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0007_customer_is_called_customer_is_mailed_invoice_token_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='status',
        ),
        migrations.AddField(
            model_name='invoice',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
