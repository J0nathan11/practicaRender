#configurando redireccionamiento
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    #Genero
    path('listadoGeneros/',views.listadoGeneros, name='listadoGeneros'),
    path('eliminarGenero/<id>',views.eliminarGenero, name='eliminarGenero'),
    path('nuevoGenero/', views.nuevoGenero, name="nuevoGenero"),
    path('guardarGenero/',views.guardarGenero, name="guardarGenero"),
    path('editarGenero/<id>',views.editarGenero, name="editarGenero"),
    path('procesarActualizacionGenero/',views.procesarActualizacionGenero, name="procesarActualizacionGenero"),

    #Pelicula
    path('listadoPeliculas/',views.listadoPeliculas, name="listadoPeliculas"),
    #Director
    path('listadoDirectores/',views.listadoDirectores, name="listadoDirectores"),
    path('eliminarDirector/<id>',views.eliminarDirector, name='eliminarDirector'),
    path('nuevoDirector/', views.nuevoDirector, name="nuevoDirector"),
    path('editarDirector/<id>',views.editarDirector, name="editarDirector"),
    path('guardarDirector/',views.guardarDirector, name="guardarDirector"),
    path('procesarActualizacionDirector/',views.procesarActualizacionDirector, name="procesarActualizacionDirector"),
    #Pais
    path('listadoPaises/',views.listadoPaises, name='listadoPaises'),
    path('nuevoPais/', views.nuevoPais, name="nuevoPais"),
    path('guardarPais/',views.guardarPais, name="guardarPais"),
    path('eliminarPais/<id>',views.eliminarPais, name='eliminarPais'),
    path('editarPais/<id>',views.editarPais, name="editarPais"),
    path('procesarActualizacionPais/',views.procesarActualizacionPais, name="procesarActualizacionPais"),

    #Gestion cines 
    path('getionCines/',views.gestionCines, name="gestionCines"),
    path('guardarCine/',views.guardarCine, name="guardarCine"),
    path('listadoCines/',views.listadoCines, name="listadoCines"),

    #Director fetch
    path('director/',views.director, name="director"),
    path('listaDirector/',views.listaDirector, name="listaDirector"),

    #Pelicula Fetch
    path('pelicula/',views.pelicula, name="pelicula"),
    path('listaPelicula/',views.listaPelicula, name="listaPelicula"),
    path('guardarPelicula/',views.guardarPelicula, name="guardarPelicula"),
 

    ]