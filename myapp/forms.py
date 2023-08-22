from django import forms

class AgregarNuevoLibro(forms.Form):
        titulo = forms.CharField(label="Titulo Libro", max_length=50)
        ISBN = forms.CharField(label="ISBN", max_length=13)
        autor = forms.CharField(label="Autor Libro", max_length=50)
        estado_libro = forms.CharField(label="Estado Libro", max_length=8)

class AgregarNuevaBiblioteca(forms.Form):
        nombre_biblioteca = forms.CharField(label="Titulo Biblioteca", max_length=50)
        ubicacion = forms.CharField(label="Ubicacion", max_length=50)

