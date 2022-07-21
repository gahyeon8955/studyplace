from django.shortcuts import render, get_object_or_404
from .models import Place

# Create your views here.

def home(request):
    return render(request, 'mainapp/home.html')

def placelist(request):
    places = Place.objects
    return render(request, 'mainapp/placelist.html', {'places':places})

def detail(request, place_id):
    place_detail = get_object_or_404(Place, pk=place_id)
    return render(request, 'mainapp/detail.html', {'place':place_detail})
