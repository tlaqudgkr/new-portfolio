from django import forms
from tourist.models import Tourist, Image

class TouristForm(forms.ModelForm):

    class Meta:
        model = Tourist
        fields = ('name', 'text', 'lon', 'lat', 'zoom', 'address')


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('image',)