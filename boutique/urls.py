from django.contrib import admin
from django.urls import path, include
from prendas.views import inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('prendas/', include('prendas.urls')),
]