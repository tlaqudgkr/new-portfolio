from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from hotel.models import Hotel, Room, Facility, Image
from hotel.form import ImageForm, HotelForm
from django.urls import reverse_lazy

# Create your views here.

class HotelListView(ListView):
    model = Hotel
    paginate_by = 10

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


def hotel_edit(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
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
        form = HotelForm(instance=hotel)
        image = ImageForm(instance=hotel)
    return render(request, 'hotel/hotel_edit.html', {'form': form, 'image': image})


class HotelDeleteView(DeleteView):
    model = Hotel
    success_url = reverse_lazy('hotel:hotel_list')



class RoomListView(ListView):
    model = Room


class FacilityListView(ListView):
    model = Facility