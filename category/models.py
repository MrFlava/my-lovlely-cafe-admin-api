from django.db import models

from restaurant.models import Restaurant


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)

    restaurant = models.ForeignKey(Restaurant, related_name="categories", on_delete=models.CASCADE)