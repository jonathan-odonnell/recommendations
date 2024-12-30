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
    cholesterol = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fibre = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    sugar = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    protein = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    vitamin_a = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    vitamin_c = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    calcium = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    iron = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    caffeine = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Sales(models.Model):
        date = models.DateField(null=True, blank=True)
        time = models.TimeField(null=True, blank=True)
        quantity = models.IntegerField(null=True, blank=True)
        store_id = models.CharField(max_length=254, null=True, blank=True)
        store_location = models.CharField(max_length=254, null=True, blank=True)	
        product_id = models.IntegerField(null=True, blank=True)	
        unit_price = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)	
        product_category = models.CharField(max_length=254, null=True, blank=True)	
        product_type = models.CharField(max_length=254, null=True, blank=True)	
        product_detail = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f'{self.store_location} - {self.date} {self.time}'
