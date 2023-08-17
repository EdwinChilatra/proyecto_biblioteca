from django import forms
from .models import Biblioteca, Libro

class BibliotecaForm(forms.ModelForm):
        model = Biblioteca
        fields = ['nombre', 'ubicacion']

class LibroForm(forms.ModelForm):
        model = Libro
        fields = ['nombre', 'isbn', 'autor', 'estado']

class NuevoLibroForm(forms.ModelForm):
        model = Libro
        fields = ['nombre', 'isbn', 'autor', 'estado']
