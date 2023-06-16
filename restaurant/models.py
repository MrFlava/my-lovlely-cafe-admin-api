from django.db import models

WEEKDAYS = [
  (1, "Monday"),
  (2, "Tuesday"),
  (3, "Wednesday"),
  (4, "Thursday"),
  (5, "Friday"),
  (6, "Saturday"),
  (7, "Sunday"),
]


class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')


class Category(models.Model):
    name = models.CharField(max_length=250)

    restaurant = models.ForeignKey(Restaurant, related_name="categories", on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=250)
    recipe = models.TextField()

    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)


class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    is_spicy = models.BooleanField(default=False)


class ProductIngredient(models.Model):
    amount = models.IntegerField(default=0)

    product = models.ForeignKey(Product, related_name="product_ingredients", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, related_name="product_ingredients", on_delete=models.CASCADE)

