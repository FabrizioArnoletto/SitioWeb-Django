from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro, Comentarios
from .forms import LibroForm, comentariosForm
from django.shortcuts import render, redirect

def inicio(request):
    libros = Libro.objects.filter(Promo = True)
    return render(request,'paginas/inicio.html', {'libros':libros})

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def crear(request):
    formulario = LibroForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros\crear.html', {'formulario':formulario})

def editar(request,id):
    libro=Libro.objects.get(ID=id)
    #recuperamos la informacion del libro
    formulario = LibroForm(request.POST or None,request.FILES or None, instance=libro)
    print(libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request,'libros/editar.html',{'formulario':formulario})

def libros(request):
    libros = Libro.objects.all()
    #print(libros)
    return render(request, 'libros/libros.html', {'libros':libros})

def eliminar(request,id):
    libro= Libro.objects.get(ID=id)
    libro.delete()
    return redirect('libros')

def comentar(request,id):
    formulario = comentariosForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros\comentar.html', {'coment':id})


def com(request,id):
    comentarios = Comentarios.objects.filter(ID=id)
    return render(request, 'libros/com.html', {'comentarios':comentarios})

def eliminarc(request,id):
    comentario= Comentarios.objects.get(ID_c=id)
    comentario.delete()
    return redirect('com')

def editarc(request,id):
    comentarios=Comentarios.objects.get(ID_c=id)
    #recuperamos la informacion del libro
    formulario = comentariosForm(request.POST or None,request.FILES or None, instance=Comentarios)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request,'libros/editarcom.html',{'formulario':formulario})