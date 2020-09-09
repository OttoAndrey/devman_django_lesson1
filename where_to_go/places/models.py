from django.db import models


class Place(models.Model):
    title = models.CharField(
        max_length=100,
    )
    description_short = models.TextField(
        max_length=280,
    )
    description_long = models.TextField()
    lng = models.DecimalField(
        max_digits=16,
        decimal_places=14,
    )
    lat = models.DecimalField(
        max_digits=16,
        decimal_places=14,
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField()
    title = models.CharField(
        max_length=100,
    )
    number = models.PositiveSmallIntegerField(
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место',
    )

    def __str__(self):
        return f'{self.number} {self.title}'
