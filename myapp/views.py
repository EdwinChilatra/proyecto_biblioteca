from django.shortcuts import render
from .models import Biblioteca, Libro
from .forms import NuevoLibroForm

def index( request ):
    title = "Django Project!!"
    return render(request, 'index.html', {
        'title': title
    })

def biblioteca ( request ):
    bibliotecas = Biblioteca.objects.all()
    return render(request, 'bibliotecas/biblioteca.html', {
        'bibliotecas': biblioteca
        })

def libros ( request ):
    libros = Libro.objects.filter(biblioteca=biblioteca)
    return render(request, 'detalles_biblioteca.html', {
        'biblioteca': biblioteca, 
        'libros': Libro
        })

def agregar_libro ( request ):
    libros = 0;

def agregar_biblioteca ( request ):
    libro = 0;

