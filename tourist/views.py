from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tourist
# Create your views here.

class TouristListView(ListView):
    model = Tourist


class TouristDetailView(DetailView):
    model = Tourist