from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Place
from .forms import PlaceNew


def home(request):
    return render(request, 'mainapp/home.html')

def placelist(request):
    places = Place.objects.all()
    paginator = Paginator(places, 1)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)
    page_range = paginator.get_elided_page_range(number=page)
    return render(request, 'mainapp/placelist.html', {'places':places,'page_range':page_range, 'page_obj': page_obj})

def detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return render(request, 'mainapp/detail.html', {'place':place})

def new(request):
    if request.method =='POST':
        form = PlaceNew(request.POST, request.FILES)
        if form.is_valid():
            place = form.save(commit=False)
            place.save()
            return redirect('/placelist/' + str(place.id))
    else:
        form = PlaceNew()
        return render(request,'mainapp/new.html',{'form':form})

def update(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    if request.method == 'POST':
        form = PlaceNew(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            return redirect('/placelist/' + str(place.id))
    else:
        form = PlaceNew(instance=place)
        return render(request, 'mainapp/update.html', {'form':form})

def delete(request, place_id):
    place = Place.objects.get(pk=place_id)
    place.delete()
    return redirect('mainapp:placelist')
