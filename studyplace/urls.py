"""studyplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import mainapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.views.home, name='home'),
    path('placelist/', mainapp.views.placelist, name='placelist'),
    path('placelist/<int:place_id>/', mainapp.views.detail, name='detail'),
    path('placelist/new/', mainapp.views.new, name='new'),
    path('placelist/create/', mainapp.views.create, name='create'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)