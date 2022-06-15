from django.contrib import admin

from .models import Refueling

# Register your models here.


@admin.register(Refueling)
class RefuelingAdmin(admin.ModelAdmin):
    list_display = [
        "mileage",
        "date_refueling",
        "price",
        "cost_per_litr",
        "tanked_to_max_level",
        "car",
    ]
