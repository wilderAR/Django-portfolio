from django.shortcuts import render, HttpResponse
from django.template import RequestContext

# Create your views here.
def inicio(request):
    return render(request,'core/assets/inicio.html')

def nosotros(request):
    return render(request,'core/assets/nosotros.html')

def login(request):
    return render(request,'core/assets/login.html')

def registro(request):
    return render(request,'core/assets/registro.html')
    
def perfil(request):
    return render(request,'core/assets/perfil.html')

def Editar(request):
        return render(request,'core/assets/editar_perfil.html')

