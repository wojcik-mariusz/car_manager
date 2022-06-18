from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView

from car.forms.car_form import CarForm, CarProductionDetailForm
from car.models import Car, CarProductionDetail


from car.services.db_services import get_all_car_obj_from_db, get_car_obj_filter_by_id

# Create your views here.


def home(request):
    context = {
        "title": "Car List",
        "cars": Car.objects.all()
    }
    return render(request, "car-home.html", context)


class CarListView(ListView):
    model = Car
    template_name = "car-home.html"
    context_object_name = "cars"


class CarDetailView(DetailView):
    model = Car
    template_name = "car-detail.html"


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "car-form.html"
    # fields = ["name", "description", "type_of_fuel", "detail"]

    def get_context_data(self, **kwargs):
        context = super(CarCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['car'] = CarForm(self.request.POST)
            context['carproductiondetail'] = CarProductionDetailForm(self.request.POST)
        else:
            context['car'] = CarForm()
            context['carproductiondetail'] = CarProductionDetailForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        carproductiondetail = context['carproductiondetail']
        if carproductiondetail.is_valid() and form.is_valid():
            f = form.save()
            shelf = carproductiondetail.save(commit=False)
            shelf.car = f
            shelf.save()
        return super().form_valid(form)

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
def edit_car(request, pk):
    if request.method == "POST":
        car = get_object_or_404(Car, pk=pk)
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
