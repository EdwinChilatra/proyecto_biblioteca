from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Biblioteca, Libro
from .forms import AgregarNuevoLibro
from .forms import AgregarNuevaBiblioteca

def index( request ):
    titulo = "Bienvenido a las Bibliotecas Del Sena"
    return render(request, 'index.html', {
        'titulo': titulo
    })

def biblioteca ( request ):
    titulo ='Bibliotecas'
    bibliotecas = Biblioteca.objects.all()
    return render(request, 'bibliotecas/biblioteca.html', {
        'titulo': titulo,
        'bibliotecas': biblioteca
        })

def libros ( request ):
    titulo ='Libros'
    libros = Libro.objects.all()
    return render(request, 'libros/libro.html', {
        'titulo': titulo,
        'libros': Libro
        })

def agregar_libro ( request ):
    titulo ='Agregar Libro'
    if request.method == 'GET':    
        return render( request, 'libros/agregar_libros.html', {
            'form': AgregarNuevoLibro()
        })
    else: 
        titulo = request.POST['titulo']
        ISBN = request.POST['ISBN']
        autor = request.POST['autor']
        estado_libro = request.POST ['estado_libro']
        id_libro = 1
        Libro.objects.create(titulo=titulo, ISBN=ISBN, id_libro=id_libro, autor=autor, estado_libro=estado_libro)
        return redirect('/libros/libro')
    
def agregar_biblioteca ( request ):
    if request.method == 'GET':    
        return render( request, 'bibliotecas/agregar_biblioteca.html', {
            'form': AgregarNuevaBiblioteca()
        })
    else: 
        nombre_biblioteca = request.POST['nombre_biblioteca']
        ubicacion = request.POST['ubicacion']
        Biblioteca.objects.create(nombre_biblioteca=nombre_biblioteca, ubicacion=ubicacion)
        return redirect('/bibliotecas/biblbioteca')

