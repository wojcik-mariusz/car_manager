from django.forms import ModelForm

from car.models import Car, CarProductionDetail


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["name", "description", "type_of_fuel"]


class CarProductionDetailForm(ModelForm):
    class Meta:
        model = CarProductionDetail
        fields = ["company", "car_model_name", "production_year", "vin"]
