from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from car_manager.forms.car_form import CarForm, CarProductionDetailForm


from car_manager.services.db_services import get_all_car_obj_from_db
# Create your views here.


def home(request):
    cars = get_all_car_obj_from_db()

    context = {
        "cars": cars
    }

    return render(request, 'home.html', context)


# TODO CRUD

@login_required
def add_new_car(request):
    print(request.user)
    car_form = CarForm(request.POST or None, initial={
        "user_name": request.user
    })
    car_production_detail_form = CarProductionDetailForm(request.POST or None)
    context = {
        "car_form": car_form,
        "car_production_detail_form": car_production_detail_form
    }

    if all((car_form.is_valid(), car_production_detail_form.is_valid())):
        car = car_form.save(commit=False)
        # car.user_name = request.user
        detail = car_production_detail_form.save()
        car.detail = detail
        car.save()

        return redirect(home)

    return render(request, 'car-form.html', context)
