from django.db import models


def valid_quantity(value):
    if value < 0 or value > 100:
        raise ValueError(f"{value} is not a valid quantity")


class Thing(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=30)
    description = models.CharField(unique=False, blank=True, max_length=120)
    quantity = models.IntegerField(unique=False, validators=[valid_quantity])
