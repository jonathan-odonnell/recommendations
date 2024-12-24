from django.db import models


class CoffeeQuality(models.Model):
    
    class Meta:
        verbose_name_plural = "Coffee Quality"

    species = models.CharField(max_length=254, null=True, blank=True)
    country = models.CharField(max_length=254, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    variety = models.CharField(max_length=254, null=True, blank=True)
    colour = models.CharField(max_length=254, null=True, blank=True)
    processing_method = models.CharField(max_length=254, null=True, blank=True)
    aroma = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    flavour = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    aftertaste = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    acidity = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    body = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    balance = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    uniformity = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    sweetness = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    moisture = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)

    def __str__(self):
        return self.name

