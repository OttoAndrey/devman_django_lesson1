# Generated by Django 3.1.1 on 2020-09-19 10:35

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20200910_2330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('number',)},
        ),
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Порядковый номер'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Описание точки'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(verbose_name='Короткое описание'),
        ),
    ]
