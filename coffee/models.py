from django.db import models


class CoffeeQuality(models.Model):
    
    class Meta:
        verbose_name_plural = "Coffee Quality"

    species = models.CharField(max_length=254)
    country_of_origin = models.CharField(max_length=254)
    year_of_harvest = models.CharField(max_length=254)
    variety = models.CharField(max_length=254)
    colour = models.CharField(max_length=254)
    processing_method = models.CharField(max_length=254)
    aroma = models.DecimalField(decimal_places=2, max_digits=4)
    flavour = models.DecimalField(decimal_places=2, max_digits=4)
    aftertaste = models.DecimalField(decimal_places=2, max_digits=4)
    acidity = models.DecimalField(decimal_places=2, max_digits=4)
    body = models.DecimalField(decimal_places=2, max_digits=4)
    balance = models.DecimalField(decimal_places=2, max_digits=4)
    unifirmity = models.DecimalField(decimal_places=2, max_digits=4)
    sweetness = models.DecimalField(decimal_places=2, max_digits=4)
    moisture = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return self.name

