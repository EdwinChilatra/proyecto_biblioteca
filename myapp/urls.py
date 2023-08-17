from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('biblioteca/', views.biblioteca, name= 'biblioteca'),
    path('libro/', views.libros, name= 'libros'),
    path('agregar_libro/', views.agregar_libro, name= 'agregar_libro'),
    path('agregar_biblioteca/', views.agregar_biblioteca, name= 'agregar_biblioteca'),

]