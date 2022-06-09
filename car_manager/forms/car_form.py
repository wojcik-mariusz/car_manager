from django.forms import ModelForm

from car_manager.models import Car, CarProductionDetail


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = []