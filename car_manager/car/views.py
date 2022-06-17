from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from car.forms.car_form import CarForm, CarProductionDetailForm
from car.models import Car, CarProductionDetail


from car.services.db_services import get_all_car_obj_from_db, get_car_obj_filter_by_id

# Create your views here.


def home(request):
    cars = get_all_car_obj_from_db()

    context = {"cars": cars}

    return render(request, "car-home.html", context)


# TODO CRUD


@login_required
def add_new_car(request):
    car_form = CarForm(request.POST or None)
    car_production_detail_form = CarProductionDetailForm(request.POST or None)
    context = {
        "car_form": car_form,
        "car_production_detail_form": car_production_detail_form,
    }

    if all((car_form.is_valid(), car_production_detail_form.is_valid())):
        car = car_form.save(commit=False)
        detail = car_production_detail_form.save()
        car.detail = detail
        car.save()

        return redirect(home)

    return render(request, "car-form.html", context)


@login_required
def edit_car(request, id):
    if request.method == "POST":
        car = get_object_or_404(Car, pk=id)
        car_form = CarForm(request.POST, instance=car)
        car_details = CarProductionDetailForm(request.POST, instance=car.detail)

        if all((car_form.is_valid(), car_details.is_valid())):
            car_form.save()
            car_details.save()
            return redirect("cars_home")

        return redirect("cars_home")

    else:
        car = get_object_or_404(Car, pk=id)
        car_form = CarForm(instance=car)
        car_details = CarProductionDetailForm(instance=car.detail)

        context = {
            "car_form": car_form,
            "car_production_detail_form": car_details,
        }

        return render(request, "car-form.html", context)
