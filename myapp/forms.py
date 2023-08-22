from django import forms
from .models import Biblioteca

class AgregarNuevoLibro(forms.Form):
        
        titulo = forms.CharField(label='Titulo del Libro', max_length=50)
        ISBN = forms.CharField(label='ISBN del Libro', max_length=13)
        autor = forms.CharField(label='Nombre del autor', max_length=50) 
        estado = forms.CharField(label='Estado del Libro', max_length=8)
        bibliotecas = forms.ModelChoiceField(label='Biblioteca', queryset=Biblioteca.objects.all())

class AgregarNuevaBiblioteca(forms.Form):
        nombre = forms.CharField(label='Nombre de la Biblioteca', max_length=50)
        ubicacion = forms.CharField(label='Ubicacion de la biblioteca', widget=forms.TextInput)

