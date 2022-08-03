from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name="mainapp"

urlpatterns = [
    path('', views.placelist, name='placelist'),
    path('<int:place_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/',views.create, name='create'),
]