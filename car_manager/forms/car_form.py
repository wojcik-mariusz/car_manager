from django.forms import ModelForm

from car_manager.models import Car, CarProductionDetail


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["name", "description", "type_of_fuel", "inssurance_expired_date", "detail"]


class CarProductionDetailForm(ModelForm):
    class Meta:
        fields = ["company", "car_model_name", "production_year", "vin"]
