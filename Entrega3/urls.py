from django.contrib import admin
from django.urls import path, include
from clientes.views import clientes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clientes.urls'))
]
