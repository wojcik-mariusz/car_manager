from django.contrib import admin

from car_manager.models import Car, CarProductionDetail
# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "type_of_fuel", "inssurance_expired_date"]


admin.register(CarProductionDetail)