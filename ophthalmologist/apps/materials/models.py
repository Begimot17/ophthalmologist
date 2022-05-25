from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    total = models.IntegerField()
    remainder = models.IntegerField()
    open = models.IntegerField()
    date_of_delivery = models.DateField('Died', null=True, blank=True)
    number_of_deliveries = models.IntegerField()
