from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Biblioteca, Libro
from .forms import AgregarNuevoLibro
from .forms import AgregarNuevaBiblioteca


def index( request ):
    title = '¡¡Bienvenido a las bibliotecas del Sena!!'
    return render( request, 'index.html', {
        'title': title,
    })

def biblioteca( request ):
    biblioteca = list(Biblioteca.objects.values())
    titulo = 'Bibliotecas'
    return render(request, 'Biblioteca/biblioteca.html',{
        'titulo':titulo,
        'biblioteca':biblioteca,
    })

def libro( request ):
    titulo = 'Libros'
    libro = Libro.objects.all()
    return render( request, 'Libros/libro.html', {
        'titulo':titulo,
        'libro':libro,
    })

def crear_Libro( request ):
    if request.method == 'GET':
        return render( request, 'Libros/crear_Libro.html', {
            'form':AgregarNuevoLibro(),
        })
    else:
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        isbn = request.POST['ISBN']
        estado = request.POST['estado']
        biblioteca = 1
        biblioteca = Biblioteca.objects.get(id=biblioteca)
        Libro.objects.create(titulo=titulo, autor=autor, ISBN=isbn, estado=estado, bibliotecas=biblioteca)
        return redirect('/libro')

def crear_Biblioteca( request ):
    if request.method == 'GET':
        return render( request, 'Biblioteca/crear_Biblioteca.html', {
            'form':AgregarNuevaBiblioteca(),
        })
    else:
        nombre = request.POST['nombre']
        ubicacion = request.POST['ubicacion']
        Biblioteca.objects.create(nombre=nombre, ubicacion=ubicacion)
        return redirect('/biblioteca')


