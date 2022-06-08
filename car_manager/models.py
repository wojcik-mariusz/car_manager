from typing import List

from django.db import models


class Car(models.Model):
    fuel_choices: List[str] = [("1", "Petrol"), ("2", "Gasoline")]

    name = models.CharField(max_length=120)
    # optional fields
    description = models.TextField(null=True, blank=True)
    type_of_fuel = models.CharField(max_length=2, choices=fuel_choices, null=True, blank=True)
    inssurance_expired_date = models.DateField(null=True, blank=True)


class CarProductionDetail(models.Model):
    company = models.TextField(null=True, blank=True)
    car_model_name = models.TextField(null=True, blank=True)
    production_year = models.IntegerField(null=True, blank=True)
    vin = models.IntegerField(null=True, blank=True)
    name = models.OneToOneField(Car, on_delete=models.CASCADE, primary_key=True)

