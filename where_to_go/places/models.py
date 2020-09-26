from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from tinymce import models as tinymce_models


class Place(models.Model):
    point_title = models.CharField(
        max_length=100,
        verbose_name='Название точки',
    )
    place_id = models.CharField(
        max_length=100,
        verbose_name='Идентификатор точки',
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
    )
    description_short = models.TextField(
        blank=True,
        verbose_name='Короткое описание',
    )
    description_long = tinymce_models.HTMLField(
        blank=True,
        verbose_name='Описание точки',
    )
    lng = models.DecimalField(
        max_digits=17,
        decimal_places=15,
        verbose_name='Долгота',
    )
    lat = models.DecimalField(
        max_digits=17,
        decimal_places=15,
        verbose_name='Ширина',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('place_detail', kwargs={'id': self.id})


class Image(models.Model):
    image = models.ImageField(
        verbose_name='Изображение'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
    )
    number = models.PositiveSmallIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name='Порядковый номер',
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место',
    )

    class Meta(object):
        ordering = ['number', ]

    def headshot_image(self):
        try:
            return format_html('<img src="{}" height="200"/>',
                               self.image.url,
                               )
        except ValueError:
            return 'Место для превью файла'

    headshot_image.short_description = 'Предизображение'

    def __str__(self):
        return f'{self.number} {self.place}'
