from django.forms import ModelForm

from refueling.models import Refueling


class RefuelingForm(ModelForm):
    class Meta:
        model = Refueling
        fields = [
            "mileage",
            "date_refueling",
            "price",
            "cost_per_litr",
            "tanked_to_max_level",
        ]
