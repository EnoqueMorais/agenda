from django.shortcuts import render
from django.http import HttpResponse
from .models import Empresa

# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def empresa_list(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas/list.html',{'empresas':empresas}) 
    
def empresa_show(request, empresa_id):
    empresa = Empresa.objects.get(pk=empresa_id)
    return render(request, 'empresas/show.html',{'empresa':empresa})  

def contato_show(request):
    return render(request, 'contato/show.html',{})

