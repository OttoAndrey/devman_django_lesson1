# Generated by Django 3.1.1 on 2020-09-30 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20200926_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='place_id',
        ),
    ]
