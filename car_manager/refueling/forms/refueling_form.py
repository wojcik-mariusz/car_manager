from django.forms import ModelForm

from refueling.models import Refueling


class RefuelingForm(ModelForm):
    """Return a ModelForm containing form fields for the given model."""
    class Meta:
        model = Refueling
        fields = [
            "mileage",
            "price",
            "cost_per_litr",
            "tanked_to_max_level",
        ]
