from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from hotel.models import Hotel, Room, Facility, Image
from hotel.form import ImageForm, HotelForm

# Create your views here.

class HotelListView(ListView):
    model = Hotel
    paginate_by = 3

class HotelDetailView(DetailView):
    model = Hotel


# class HotelCreateView(CreateView):
#     model = Hotel
#     fields = ['name', 'text', 'lon', 'lat', 'zoom', 'site']

def hotel_create(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.save()

            upimgs = request.FILES.getlist('image')
            for upimg in upimgs:
                img = Image()
                img.image = upimg
                img.hotel = hotel
                img.save()
            return redirect('hotel:hotel_detail', pk=hotel.pk)
    else:
        form = HotelForm()
        image = ImageForm()
    return render(request, 'hotel/hotel_edit.html', {'form': form, 'image': image})


class RoomListView(ListView):
    model = Room


class FacilityListView(ListView):
    model = Facility