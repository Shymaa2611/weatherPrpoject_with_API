# Generated by Django 4.2.2 on 2023-06-24 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='relation',
        ),
        migrations.DeleteModel(
            name='Weather',
        ),
    ]
