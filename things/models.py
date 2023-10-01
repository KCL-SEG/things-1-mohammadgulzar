from django.db import models


def valid_quantity(value):
    return value >= 0 and value <= 100


class Thing(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=30)
    description = models.CharField(unique=False, blank=True, max_length=120)
    quantity = models.IntegerField(unique=False, validators=[valid_quantity])
