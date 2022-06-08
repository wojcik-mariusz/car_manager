from typing import List

from django.db import models


class Car(models.Model):
    fuel_choices: List[str] = ["Petrol", "Gasoline"]

    name = models.CharField(max_length=120)
    # optional fields
    description = models.TextField(null=True, blank=True)
    type_of_fuel = models.CharField(choices=fuel_choices, null=True, blank=True)
    company = models.TextField(null=True, blank=True)
    car_model_name = models.TextField(null=True, blank=True)
    production_year = models.IntegerField(null=True, blank=True)
    vin = models.IntegerField(null=True, blank=True)
    inssurance_expired_date = models.DateField(null=True, blank=True)
