from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from refueling.models import Refueling
from refueling.forms.refueling_form import RefuelingForm

from car.models import Car

# Create your views here.


class RefuelingListView(ListView):
    model = Refueling
    template_name = "refuelings.html"
    context_object_name = "refuelings"


# TODO mixins, login, userpassestest
class RefuelingCreateView(CreateView):
    model = Refueling
    refueling_form = RefuelingForm
    fields = "__all__"
    template_name = "refueling-form.html"

    def post(self, request, *args, **kwargs):
        refueling_form = self.refueling_form(request.POST)

        if refueling_form.is_valid():
            refueling = refueling_form.save(commit=False)
            refueling.car = get_object_or_404(Car, pk=self.kwargs["pk"])
            refueling.save()
            return redirect("all-refuelings")

    def get_context_data(self, **kwargs):
        context = super(RefuelingCreateView, self).get_context_data(**kwargs)
        context["refueling_form"] = self.refueling_form
        context["car"] = get_object_or_404(Car, pk=self.kwargs["pk"])
        return context

    def form_invalid(self, form):
        return JsonResponse({"success": False})


# TODO mixins, login, userpassestest
# TODO submit button should be named as 'apply changes'
class RefuelingUpdateView(UpdateView):
    model = Refueling
    form_class = RefuelingForm
    template_name = "refueling-form.html"
    success_url = reverse_lazy("all-refuelings")

    def get_context_data(self, **kwargs):
        context = super(RefuelingUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["refueling_form"] = RefuelingForm(
                self.request.POST,
                instance=get_object_or_404(Refueling, pk=self.kwargs["pk"]),
            )
        else:
            context["refueling_form"] = RefuelingForm(
                instance=get_object_or_404(Refueling, pk=self.kwargs["pk"])
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        refueling = context["refueling_form"]
        refueling.car = get_object_or_404(Refueling, pk=self.kwargs["pk"]).car
        refueling.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return JsonResponse({"success": False})


class RefuelingDeleteView(DeleteView):
    model = Refueling
    template_name = "refueling_confirm_delete.html"
    success_url = reverse_lazy("all-refuelings")
