from django.db import models

# Create your models here.
class Readout(models.Model):
    time = models.DateTimeField()
    pulsometer = models.FloatField()
    efficiency = models.FloatField()
    red_value = models.IntegerField()
    green_value = models.IntegerField()
    blue_value = models.IntegerField()