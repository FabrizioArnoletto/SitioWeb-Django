from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from django.shortcuts import render, redirect

def inicio(request):
    return render(request,'paginas/inicio.html')

def sesion(request):
    return render(request,'paginas/sesion.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def crear(request):
    formulario = LibroForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("{%url 'libros'%}")
    return render(request, 'libros/crear.html', {'formulario':formulario})

def editar(request,id):
    libro=Libro.objects.get(id=id)
    #recuperamos la informacion del libro
    formulario = LibroForm(request.POST or None,request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST : 
        formulario.save()
        return redirect('libros')
    return render(request,'libros/editar.html',{'formulario':formulario})

def form(request):
    return render(request,'libros/form.html')


def libros(request):
    libros = Libro.objects.all()
    print(libros)
    return render(request, 'libros/libros.html', {'libros':libros})

def eliminar(request,id):
    libro= Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')