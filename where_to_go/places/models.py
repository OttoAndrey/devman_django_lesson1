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
