from django import forms
from .models import Category, Place

class PlaceNew(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name','address', 'phone_number', 'business_hour', 'photo', 'category']
