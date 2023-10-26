from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from django.shortcuts import render, redirect

def libros(request):
    libros = Libro.objects.all()
    print(libros)
    return render(request, 'libros/libros.html')

def libros(request):
    libros = Libro.objects.all()
    print(libros)
    return render(request, 'libros/libros.html', {'libros':libros})

def inicio(request):
    return render(request,'paginas/inicio.html')

def sesion(request):
    return render(request,'paginas/sesion.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def librosc(request):
    formulario = LibroForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("{%url 'libros'%}")
    return render(request, 'libros/crear.html', {'formulario':formulario})

def librose(request,id):
    libro=Libro.objects.get(id=id)
    #recuperamos la informacion del libro
    formulario = LibroForm(request.POST or None,request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST : 
        formulario.save()
        return redirect('libros')
    return render(request,'libros/editar.html',{'formulario':formulario})

def librosf(request):
    return render(request,'libros/form.html')


def libros(request):
    libros = Libro.objects.all()
    print(libros)
    return render(request, 'libros/libros.html', {'libros':libros})