from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Place, Category
from .forms import PlaceNew


def home(request):
    return render(request, 'mainapp/home.html')

def placelist(request, category_name):
    categories = Category.objects.all()
    category = get_object_or_404(Category, name=category_name)
    places = Place.objects.filter(category=category)

    paginator = Paginator(places, 6)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)
    page_range = paginator.get_elided_page_range(number=page)
    context = {
        'places':places,'page_range':page_range, 'page_obj': page_obj, "category_name": category_name,
            "categories": categories,
    }
    return render(request, 'mainapp/placelist.html', context)

# def placelist(request, category_name):
#     categories = Category.objects.all()
#     category = get_object_or_404(Category, name=category_name)
#     places = Place.objects.filter(category=category)

#     paginator = Paginator(places, 6)
#     page = request.GET.get('page',1)
#     page_obj = paginator.page(page)
#     page_range = paginator.get_elided_page_range(number=page)
#     return render(request, 'mainapp/placelist.html', {'places':places,'page_range':page_range, 'page_obj': page_obj, "category_name": category_name,
#             "categories": categories,})

def detail(request, category_name, place_id):
    place = get_object_or_404(Place, pk=place_id)
    category = get_object_or_404(Category, name=category_name)
    return render(request, 'mainapp/detail.html', {'place':place, 'category':category})

def new(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    if request.method =='POST':
        form = PlaceNew(request.POST, request.FILES)
        if form.is_valid():
            place = form.save(commit=False)
            place.save()
            return redirect('/placelist/' + str(category.name) + '/' + str(place.id))
    else:
        form = PlaceNew()
        return render(request,'mainapp/new.html',{'form':form})

def update(request, place_id, category_name):
    place = get_object_or_404(Place, pk=place_id)
    category = get_object_or_404(Category, name=category_name)
    if request.method == 'POST':
        form = PlaceNew(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            return redirect('/placelist/' + str(category.name) + '/' + str(place.id))
    else:
        form = PlaceNew(instance=place)
        return render(request, 'mainapp/update.html', {'form':form})

def delete(request, category_name, place_id):
    place = Place.objects.get(pk=place_id)
    category = get_object_or_404(Category, name=category_name)
    place.delete()
    return redirect('/placelist/' + str(category.name))
