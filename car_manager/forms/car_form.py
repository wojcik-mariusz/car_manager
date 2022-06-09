from django.forms import ModelForm

from car_manager.models import Car, CarProductionDetail


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["name", "description", "type_of_fuel", "inssurance_expired_date", "user_name"]


class CarProductionDetailForm(ModelForm):
    class Meta:
        model = CarProductionDetail
        fields = ["company", "car_model_name", "production_year", "vin"]
