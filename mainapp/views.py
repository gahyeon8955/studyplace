from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Place
from .forms import PlaceNew


def home(request):
    return render(request, 'mainapp/home.html')

def placelist(request):
    places = Place.objects
    return render(request, 'mainapp/placelist.html', {'places':places})

def detail(request, place_id):
    place_detail = get_object_or_404(Place, pk=place_id)
    return render(request, 'mainapp/detail.html', {'place':place_detail})

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

# def create(request):
#     place = Place()
#     place.name = request.GET['name']
#     place.address = request.GET['address']
#     place.phone_number = request.GET['phone_number']
#     place.business_hour = request.GET['business_hour']
#     place.save()
#     return redirect('/placelist/' + str(place.id))