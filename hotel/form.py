from django import forms
from hotel.models import Image, Hotel

class HotelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        fields = ('name', 'text', 'lon', 'lat', 'zoom', 'site')


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('image',)