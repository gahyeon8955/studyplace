from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name="mainapp"

urlpatterns = [
    path('<str:category_name>/', views.placelist, name='placelist'),
    path('<str:category_name>/<int:place_id>/', views.detail, name='detail'),
    path('<str:category_name>/new/', views.new, name='new'),
    path('<str:category_name>/<int:place_id>/update/', views.update, name='update'),
    path('<str:category_name>/<int:place_id>/delete/', views.delete, name='delete'),
]