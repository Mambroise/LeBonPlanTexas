# Generated by Django 5.1.4 on 2025-01-05 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0008_remove_invoice_status_invoice_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='terms_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
