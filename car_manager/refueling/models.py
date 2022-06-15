from django.db import models

from datetime import datetime as dt

# Create your models here.


class Refueling(models.Model):
    mileage = models.IntegerField()
    date_refueling = models.DateField(default=dt.now())
    cost_per_litr = models.DecimalField(decimal_places=2, blank=False, null=False)
    tanked_to_max_level = models.BooleanField(default=False)

