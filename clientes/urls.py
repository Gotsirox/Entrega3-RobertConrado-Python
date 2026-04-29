from django.urls import path
from clientes.views import *

urlpatterns=[
    path('', clientes, name='inicio'),
    path('listado/', clientes_listado, name='listado'),
    path('formulario/', clientes_formulario, name='form'),
]