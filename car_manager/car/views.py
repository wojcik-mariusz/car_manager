from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from car.forms.car_form import CarForm, CarProductionDetailForm
from car.models import Car, CarProductionDetail


def home(request):
    context = {"title": "Car List", "cars": Car.objects.all()}
    return render(request, "car_list.html", context)


class CarListView(ListView):
    model = Car
    template_name = "car_list.html"
    context_object_name = "cars"


class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"


class CarCreateView(CreateView, LoginRequiredMixin):
    model = Car
    car_form = CarForm
    car_prod_det_form = CarProductionDetailForm
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        car_form = self.car_form(request.POST)
        car_prod_det_form = self.car_prod_det_form(request.POST)

        if all([car_form.is_valid(), car_prod_det_form.is_valid()]):
            car_details = car_prod_det_form.save(commit=False)
            car_details.save()
            car = car_form.save(commit=False)
            car.detail = car_details
            car.save()
            return redirect("cars-list")
        return self.form_invalid(**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["car_form"] = self.car_form
        context["car_prod_det_form"] = self.car_prod_det_form
        return context

    def form_invalid(self, **kwargs):
        return JsonResponse({"success": False})


class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = "car-form.html"
    success_url = "/cars/"

    def get_context_data(self, **kwargs):
        context = super(CarUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["car"] = CarForm(self.request.POST)
            context["carproductiondetail"] = CarProductionDetailForm(self.request.POST)
        else:
            context["car"] = CarForm(
                instance=get_object_or_404(Car, pk=self.kwargs["pk"])
            )
            context["carproductiondetail"] = CarProductionDetailForm(
                instance=get_object_or_404(Car, pk=self.kwargs["pk"]).detail
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        carproductiondetail = context["carproductiondetail"]
        if carproductiondetail.is_valid() and form.is_valid():
            f = form.save()
            shelf = carproductiondetail.save(commit=False)
            shelf.car = f
            shelf.save()
        return super().form_valid(form)


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = CarProductionDetail
    success_url = "/cars/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = get_object_or_404(Car, pk=self.kwargs["pk"])

        context["carproductiondetail"] = get_object_or_404(
            Car, pk=self.kwargs["pk"]
        ).detail

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        return super(CarDeleteView, self).form_valid(context)


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
            return redirect("cars-list")

        return redirect("cars-list")

    else:
        car = get_object_or_404(Car, pk=id)
        car_form = CarForm(instance=car)
        car_details = CarProductionDetailForm(instance=car.detail)

        context = {
            "car_form": car_form,
            "car_production_detail_form": car_details,
        }

        return render(request, "car-form.html", context)
