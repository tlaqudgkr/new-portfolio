from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from hotel.models import Hotel, Room, Facility

# Create your views here.

class HotelListView(ListView):
    model = Hotel


class HotelDetailView(DetailView):
    model = Hotel


class RoomListView(ListView):
    model = Room


class FacilityListView(ListView):
    model = Facility


