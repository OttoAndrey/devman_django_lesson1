from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from tinymce import models as tinymce_models


class Place(models.Model):
    point_title = models.CharField(
        max_length=100,
        verbose_name='Название точки',
        help_text='При наведении курсором на точку будет отображаться это название.'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
        help_text='Заголовок в описании.'
    )
    short_description = models.TextField(
        blank=True,
        verbose_name='Короткое описание',
    )
    long_description = tinymce_models.HTMLField(
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
        db_index=True,
        verbose_name='Порядковый номер',
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место',
    )

    def get_preview_image(self):
        try:
            return format_html('<img src="{}" height="200"/>',
                               self.image.url,
                               )
        except ValueError:
            return 'Место для превью файла'

    get_preview_image.short_description = 'Предизображение'

    def __str__(self):
        return f'{self.number} {self.place}'

    class Meta(object):
        ordering = ['number', ]
