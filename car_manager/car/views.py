from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

    def get_queryset(self):
        return Car.objects.filter(user_name=self.request.user.username)


class CarDetailView(DetailView):
    model = Car
    template_name = "car-detail.html"

    def get_queryset(self):
        return Car.objects.filter(user_name=self.request.user.username)


class CarCreateView(CreateView, LoginRequiredMixin):
    model = Car
    car_form = CarForm
    car_prod_det_form = CarProductionDetailForm
    fields = "__all__"
    template_name = "car/car-form.html"

    def post(self, request, *args, **kwargs):
        car_form = self.car_form(request.POST)
        car_prod_det_form = self.car_prod_det_form(request.POST)

        if all([car_form.is_valid(), car_prod_det_form.is_valid()]):
            car_details = car_prod_det_form.save(commit=False)
            car_details.save()
            car = car_form.save(commit=False)
            car.user_name = request.user.username
            car.detail = car_details
            car.save()
            return redirect("cars-list")
        return self.form_invalid(car_form)

    def get_context_data(self):
        context = super().get_context_data()
        context["car_form"] = self.car_form
        context["car_prod_det_form"] = self.car_prod_det_form
        return context

    def form_invalid(self, form):
        return JsonResponse({"success": False})


class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = "car/car-form.html"
    success_url = "/cars/"

    def get_context_data(self, **kwargs):
        context = super(CarUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["car_form"] = CarForm(self.request.POST)
            context["car_prod_det_form"] = CarProductionDetailForm(
                self.request.POST
            )
        else:
            context["car_form"] = CarForm(
                instance=get_object_or_404(Car, pk=self.kwargs["pk"])
            )
            context["car_prod_det_form"] = CarProductionDetailForm(
                instance=get_object_or_404(Car, pk=self.kwargs["pk"]).detail
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        carproductiondetail = context["car_prod_det_form"]
        if carproductiondetail.is_valid() and form.is_valid():
            f = form.save()
            shelf = carproductiondetail.save(commit=False)
            shelf.car = f
            shelf.save()
        return super().form_valid(form)

    def test_func(self):
        car = self.get_object()
        return self.request.user.username == car.user_name


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = CarProductionDetail
    success_url = "/cars/"
    template_name = "car/carproductiondetail_confirm_delete.html"

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
