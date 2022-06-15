from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Refueling

# Create your views here.


class RefuelingListView(ListView):
    model = Refueling
    template_name = "refuelings.html"
    context_object_name = "refuelings"
