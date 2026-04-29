from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from clientes.models import cliente
from clientes.forms import form_client, form_search

# Create your views here.
def clientes(request):

    date_time=datetime.now()
    lista=  cliente.objects.all()
    
    return render(request, 'clientes/inicio.html',{'date_time':date_time,'lista':lista})

def clientes_listado(request):

    date_time=datetime.now()
    lista=  cliente.objects.all()
    
    formulario=form_search(request.GET)
    if formulario.is_valid():
        data=formulario.cleaned_data
        lista=cliente.objects.filter(names__icontains=data.get('names'),surnames__icontains=data.get('surnames'),client_id__icontains=data.get('client_id'),salary__icontains=data.get('salary'))
    else:
        lista=cliente.objects.all()


    return render(request, 'clientes/clientes_listado.html',{'date_time':date_time,'lista':lista,'formulario':formulario})

def clientes_formulario(request):
    date_time=datetime.now()
    if request.method=='POST':
        formulario=form_client(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            clientes=cliente(names=data.get('names'), surnames=data.get('surnames'), client_id=data.get('client_id'), dat_ini=data.get('dat_ini'),salary=data.get('salary'))
            clientes.save()
    else:
        formulario=form_client()

    return render(request, 'clientes/clientes_formulario.html',{'date_time':date_time,'formulario':formulario})