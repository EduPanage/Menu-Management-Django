from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="menu_items",
    )
    category = models.CharField(max_length=45)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"
