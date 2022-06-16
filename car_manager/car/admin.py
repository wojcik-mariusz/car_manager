from django.contrib import admin

from car.models import Car, CarProductionDetail

# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "type_of_fuel"]


admin.site.register(CarProductionDetail)
