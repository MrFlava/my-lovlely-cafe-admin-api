from django.db import models

from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField(default=0.0)
    recipe = models.TextField()

    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)


class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    is_spicy = models.BooleanField(default=False)


class ProductIngredient(models.Model):
    amount = models.IntegerField(default=0)

    product = models.ForeignKey(Product, related_name="product_ingredients", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, related_name="product_ingredients", on_delete=models.CASCADE)

