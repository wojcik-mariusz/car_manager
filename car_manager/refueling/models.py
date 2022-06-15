from django.db import models
from django.utils import timezone

from car.models import Car

# Create your models here.


class Refueling(models.Model):
    mileage = models.IntegerField()
    date_refueling = models.DateField(default=timezone.now())
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    cost_per_litr = models.DecimalField(
        max_digits=4, decimal_places=2, blank=False, null=False
    )
    tanked_to_max_level = models.BooleanField(default=False)
    car = models.OneToOneField(Car, on_delete=models.CASCADE, null=True, blank=False)
