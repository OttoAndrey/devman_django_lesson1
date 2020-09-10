# Generated by Django 3.1.1 on 2020-09-10 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20200910_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_id',
            field=models.CharField(default=123, max_length=50, verbose_name='Идентификатор точки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='point_title',
            field=models.CharField(default=123, max_length=50, verbose_name='Название точки'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.PositiveSmallIntegerField(verbose_name='Порядковый номер'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=models.TextField(verbose_name='Описание точки'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(max_length=280, verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.DecimalField(decimal_places=15, max_digits=17, verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.DecimalField(decimal_places=15, max_digits=17, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
