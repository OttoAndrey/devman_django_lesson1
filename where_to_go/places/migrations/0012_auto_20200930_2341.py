# Generated by Django 3.1.1 on 2020-09-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_auto_20200930_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.PositiveSmallIntegerField(db_index=True, default=0, verbose_name='Порядковый номер'),
        ),
    ]