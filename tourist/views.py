from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from .models import Tourist, Image
from tourist.form import TouristForm, ImageForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class TouristListView(ListView):
    model = Tourist
    paginate_by = 3

@method_decorator(login_required, name='dispatch')
class TouristDetailView(DetailView):
    model = Tourist

@login_required
def tourist_create(request):
    if request.method == 'POST':
        form = TouristForm(request.POST)
        if form.is_valid():
            tourist = form.save(commit=False)
            tourist.save()

            upimgs = request.FILES.getlist('image')
            for upimg in upimgs:
                img = Image()
                img.image = upimg
                img.tourist = tourist
                img.save()
            return redirect('tourist:tourist_detail', pk=tourist.pk)
    else:
        form = TouristForm()
        image = ImageForm()
    return render(request, 'tourist/tourist_edit.html', {'form':form, 'image':image})

@login_required
def tourist_edit(request, pk):
    tourist = get_object_or_404(Tourist, pk=pk)
    if request.method == 'POST':
        form = TouristForm(request.POST, instance=tourist)
        if form.is_valid():
            tourist = form.save(commit=False)
            tourist.save()

            upimgs = request.FILES.getlist('image')
            for upimg in upimgs:
                img = Image()
                img.image = upimg
                img.tourist = tourist
                img.save()
            return redirect('tourist:tourist_detail', pk=tourist.pk)
    else:
        form = TouristForm(instance=tourist)
        image = ImageForm(instance=tourist)
    return render(request, 'tourist/tourist_edit.html', {'form':form, 'image':image})

@method_decorator(login_required, name='dispatch')
class TouristDeleteView(DeleteView):
    model = Tourist
    success_url = reverse_lazy('tourist:tourist_list')