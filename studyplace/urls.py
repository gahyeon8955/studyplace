from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import mainapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.views.home, name='home'),
    path('placelist/', include('mainapp.urls')),
    path('accounts/', include('accounts.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)