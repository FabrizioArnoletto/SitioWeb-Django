from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request,'paginas/inicio.html')

def sesion(request):
    return render(request,'paginas/sesion.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def libros(request):
    return render(request,'libros/libros.html')

def librosc(request):
    return render(request,'libros/crear.html')

def librose(request):
    return render(request,'libros/editar.html')

def librosf(request):
    return render(request,'libros/form.html')