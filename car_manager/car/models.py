import datetime
from typing import List

from django.db import models


class CarProductionDetail(models.Model):
    company = models.CharField(null=True, blank=True, max_length=250)
    car_model_name = models.CharField(null=True, blank=True, max_length=250)
    production_year = models.IntegerField(null=True, blank=True)
    vin = models.CharField(null=True, blank=True, max_length=17)

    def __str__(self) -> str:
        return f"{self.company} {self.car_model_name} ({self.production_year})"


class Car(models.Model):
    fuel_choices: List[str] = [("1", "Petrol"), ("2", "Gasoline")]

    name = models.CharField(max_length=120, unique=True)
    # optional fields
    description = models.CharField(null=True, blank=True, max_length=250)
    type_of_fuel = models.CharField(max_length=2, choices=fuel_choices, null=True, blank=True)
    detail = models.OneToOneField(CarProductionDetail, on_delete=models.CASCADE, null=True, blank=True)
