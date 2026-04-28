from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime

# Create your views here.
def inicio(request):

    date_time=datetime.now()
    lista= list(range(1,11))
    
    return render(request, 'inicio.html',{'date_time':date_time,'lista':lista})
