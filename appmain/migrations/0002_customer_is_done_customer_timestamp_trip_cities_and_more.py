# Generated by Django 5.1.4 on 2024-12-11 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='cities',
            field=models.CharField(max_length=255, null=True, verbose_name='Villes:'),
        ),
        migrations.AddField(
            model_name='trip',
            name='comment',
            field=models.TextField(max_length=500, null=True, verbose_name='Commentaire:'),
        ),
        migrations.AddField(
            model_name='trip',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trip',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Portable:'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateField(verbose_name='Date de fin:'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateField(verbose_name='Date de début:'),
        ),
    ]
