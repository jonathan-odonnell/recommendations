from django.db import models


class Nutrient(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    units = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.name


class Stat(models.Model):
    category = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    prep = models.CharField(max_length=254, null=True, blank=True)
    calories = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    total_fat = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    trans_fat = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    saturated_fat = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    sodium = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cholestorol = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fibre = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    sugar =models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    protein = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    vitimin_a = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    vitimin_c = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    calcium = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    iron = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    caffeine = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.beverage
