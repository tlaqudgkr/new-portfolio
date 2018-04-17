from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from hotel.models import Hotel, Room, Facility, Image

# Create your views here.

class HotelListView(ListView):
    model = Hotel

class HotelDetailView(DetailView):
    model = Hotel


class HotelCreateView(CreateView):
    model = Hotel
    fields = ['name', 'text', 'lon', 'lat', 'zoom', 'site']

    # model = Image
    # fields = ['image']

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['image'] = Image.objects.all()
    #     return context


class RoomListView(ListView):
    model = Room


class FacilityListView(ListView):
    model = Facility