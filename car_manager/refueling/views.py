from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import QuerySet

from typing import Union, List

from refueling.models import Refueling
from refueling.forms.refueling_form import RefuelingForm
from car.models import Car


class RefuelingListView(LoginRequiredMixin, ListView):
    """
        Render list of objects, set by `self.queryset`.
        `self.queryset` can actually be any iterable of items, not just a queryset.

        **Template:**

        :template:`car_manager/refueling/templates/refuelings.html`
    """
    model = Refueling
    template_name = "refuelings.html"
    context_object_name = "refuelings"

    def get_queryset(self) -> Union[QuerySet, List[Refueling]]:
        """
        Return the list of items for this view.

        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.

        Returns QuerySet of :model:'refueling.Refueling'
        when car is created by requested user.
        """
        return Refueling.objects.filter(
            car__user_name=self.request.user.username
        )


class RefuelingListViewFilterByCar(LoginRequiredMixin, ListView):
    """
            Render list of objects, set by `self.queryset`.
            `self.queryset` can actually be any iterable of items, not just a queryset.

            **Template:**

            :template:`car_manager/refueling/templates/refuelings-by-car.html`
    """
    model = Refueling
    template_name = "refuelings-by-car.html"
    context_object_name = "refuelings"

    def get_queryset(self) -> Union[QuerySet, List[Refueling]]:
        """
            Return the list of items for this view.

            The return value must be an iterable and may be an instance of
            `QuerySet` in which case `QuerySet` specific behavior will be enabled.

            Returns QuerySet of :model:'refueling.Refueling'
            when car is created by requested user, and refueling is assigned to car.
        """
        return Refueling.objects.filter(
            car__user_name=self.request.user.username,
            car__id=self.kwargs["pk"]
        )


class RefuelingCreateView(LoginRequiredMixin, CreateView):
    """
        View to create :model:'refueling.Refueling'. User must be logged.

        **Template:**

        :template:`car_manager/refueling/templates/refueling-form.html`
    """
    model = Refueling
    refueling_form = RefuelingForm
    fields = "__all__"
    template_name = "refueling-form.html"

    def post(self, request, *args, **kwargs):
        """
            Handle POST requests: instantiate a form instance with the passed
            POST variables and then check if it's valid.
        """
        refueling_form = self.refueling_form(request.POST)

        if refueling_form.is_valid():
            refueling = refueling_form.save(commit=False)
            refueling.car = get_object_or_404(Car, pk=self.kwargs["pk"])
            refueling.save()
            return redirect("all-refuelings")

    def get_context_data(self, **kwargs) -> dict:
        """Insert the single object into the context dict."""
        context = super(RefuelingCreateView, self).get_context_data(**kwargs)
        context["refueling_form"] = self.refueling_form
        context["car"] = get_object_or_404(Car, pk=self.kwargs["pk"])
        context["new_object"] = True
        return context

    def form_invalid(self, form):
        return JsonResponse({"success": False})


class RefuelingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
        View for updating an object, with a response rendered by a template.

        **Template:**

        :template: 'car_manager/car/templates/car/refueling-form.html'
    """
    model = Refueling
    form_class = RefuelingForm
    template_name = "refueling-form.html"
    success_url = reverse_lazy("all-refuelings")

    def get_context_data(self, **kwargs) -> Union[QuerySet, List[Refueling]]:
        """Insert the single object into the context dict."""
        context = super(RefuelingUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["refueling_form"] = RefuelingForm(
                self.request.POST,
                instance=get_object_or_404(Refueling, pk=self.kwargs["pk"]),
            )
            context["new_object"] = False
        else:
            context["refueling_form"] = RefuelingForm(
                instance=get_object_or_404(Refueling, pk=self.kwargs["pk"])
            )
        return context

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        context = self.get_context_data()
        refueling = context["refueling_form"]
        refueling.car = get_object_or_404(Refueling, pk=self.kwargs["pk"]).car
        refueling.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return JsonResponse({"success": False})

    def test_func(self) -> bool:
        """
            Deny a request with a permission error if the test_func() method returns
            False.
        """
        refueling = self.get_object()
        return self.request.user.username == refueling.car.user_name


class RefuelingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
        View for deleting an object retrieved with self.get_object(), with a
        response rendered by a template.

        **Template:**

        :template: 'refueling/templates/refueling_confirm_delete.html'
    """
    model = Refueling
    template_name = "refueling_confirm_delete.html"
    success_url = reverse_lazy("all-refuelings")

    def test_func(self) -> bool:
        """
            Deny a request with a permission error if the test_func() method returns
            False.
        """
        refueling = self.get_object()
        return self.request.user.username == refueling.car.user_name
