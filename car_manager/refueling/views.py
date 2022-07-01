from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import CreateView

from .models import Refueling

# Create your views here.


class RefuelingListView(ListView):
    model = Refueling
    template_name = "refuelings.html"
    context_object_name = "refuelings"


class RefuelingCreateView(CreateView):
    model = Refueling
    template_name =
