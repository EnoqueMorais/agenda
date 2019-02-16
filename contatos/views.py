from django.shortcuts import render, redirect
from .models import Empresa
from .forms import EmpresaForm

# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def empresa_list(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas/list.html',{'empresas':empresas}) 
    
def empresa_show(request, empresa_id):
    empresa = Empresa.objects.get(pk=empresa_id)
    return render(request, 'empresas/show.html',{'empresa':empresa})  

def empresa_form(request): 
    if (request.method == 'POST'):
        form = EmpresaForm(request.POST)
        if (form.is_valid()):
            form.save() 
            return redirect('/contatos/empresas')          
        else:
            return render(request,'empresas/form.html', {'form':form})
    else:
        form = EmpresaForm()
        return render(request,'empresas/form.html', {'form': form}) 

def empresa_edit(request, empresa_id):
    if (request.method == 'POST'):
        empresa = Empresa.objects.get(pk=empresa_id)
        form = EmpresaForm(request.POST, instance=empresa)
        if (form.is_valid()):
            form.save() 
            return redirect('/contatos/empresas/')          
        else:
            return render(request,'empresas/edit.html', {'form': form, 'empresa_id':empresa_id})
    else:
        empresa = Empresa.objects.get(pk=empresa_id)
        form = EmpresaForm(instance=empresa)
        return render(request, 'empresas/edit.html',{'form': form, 'empresa_id':empresa_id})



 

def contato_show(request):
    return render(request, 'contato/show.html',{})


