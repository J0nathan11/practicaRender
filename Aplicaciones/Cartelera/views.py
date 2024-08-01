from typing import Counter
from django.shortcuts import render, redirect
from .models import Genero,Pelicula,Director,Pais,Cine
from django.contrib import messages 
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

#---------------------Genero-------------------------------------------------------
# Renderizando el template de ListadoGenero
def listadoGeneros(request):
    generosBdd = Genero.objects.all()
    # Contar descripciones por cada género
    genero_counts = Counter([genero.nombre for genero in generosBdd])
    context = {
        'generos': generosBdd,
        'nombres': list(genero_counts.keys()), # Nombres de los géneros
        'descripciones_count': list(genero_counts.values()) # Conteo de descripciones por género
    }
    return render(request, 'listadoGeneros.html', context)

#Nuevo Genero formulario
def nuevoGenero(request):
    return render(request, 'nuevoGenero.html')
#Insertar datos en la bdd
def guardarGenero(request):
    nom=request.POST['nombre']
    desc=request.POST['descripcion']
    fot=request.FILES.get("foto")
    nuevoGenero=Genero.objects.create(nombre=nom,descripcion=desc,foto=fot)
    messages.success(request, 'Genero guardado con éxito')
    return redirect('listadoGeneros')
#Genero Eliminar
def eliminarGenero(request,id):
    generoEliminar = Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request, 'Genero eliminado con éxito')
    return redirect('listadoGeneros')
#Genero Editar
def editarGenero(request,id):
    generoEditar = Genero.objects.get(id=id)
    return render(request, 'editarGenero.html', {'generoEditar':generoEditar})
#Actualizando datos Genero 
def procesarActualizacionGenero(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    foto=request.FILES.get("foto")
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nombre
    generoConsultado.descripcion=descripcion
    generoConsultado.foto=foto
    generoConsultado.save()
    messages.success(request, 'Genero actualizado con éxito')
    return redirect('listadoGeneros')


#----------------------Pais---------------------------------------------------------
# Renderizando el template de ListadoPaises
def listadoPaises(request):
    paisesBdd=Pais.objects.all()
    return render(request,'listadoPaises.html', {'paises':paisesBdd})
#Nuevo Pais formulario 
def nuevoPais(request):
    return render(request, 'nuevoPais.html')
#Guardar Pais
def guardarPais(request):
    nom=request.POST['nombre']
    cont=request.POST['continente']
    capt=request.POST['capital']
    nuevoPais=Pais.objects.create(nombre=nom,continente=cont,capital=capt)
    messages.success(request, 'Pais guardado con éxito')
    return redirect('listadoPaises')
#Eliminar Pais 
def eliminarPais(request,id):
    paisEliminar = Pais.objects.get(id=id)
    paisEliminar.delete()
    messages.success(request, 'Pais eliminado con éxito')
    return redirect('listadoPaises')
#Editar Pais
def editarPais(request,id):
    paisEditar = Pais.objects.get(id=id)
    return render(request, 'editarPais.html', {'paisEditar':paisEditar})
#Actualizando datos Pais
def procesarActualizacionPais(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    continente=request.POST['continente']
    capital=request.POST['capital']
    paisConsultado=Pais.objects.get(id=id)
    paisConsultado.nombre=nombre
    paisConsultado.continente=continente
    paisConsultado.capital=capital
    paisConsultado.save()
    messages.success(request, 'Pais actualizado con éxito')
    return redirect('listadoPaises')



#---------------------Pelicula---------------------------------------------------
def listadoPeliculas(request):
    peliculasBdd=Pelicula.objects.all()
    return render(request,'listadoPeliculas.html', {'peliculas':peliculasBdd})



    
#---------------------Director------------------------------------------------
# Renderizando el template de ListadoDirectores
def listadoDirectores(request):
    directoresBdd=Director.objects.all()
    return render(request,'listadoDirectores.html', {'directores':directoresBdd})
#Director Nuevo formulario
def nuevoDirector(request):
    return render(request, 'nuevoDirector.html')
#Guardar Director
def guardarDirector(request):
    dni=request.POST['dni']
    nom=request.POST['nombre']
    ape=request.POST['apellido']
    fot=request.FILES.get("foto")
    nuevoDirector=Director.objects.create(dni=dni,nombre=nom,apellido=ape,foto=fot)
    messages.success(request, 'Director guardado con éxito')
    return redirect('listadoDirectores')
#Eliminar Director
def eliminarDirector(request,id):
    directorEliminar = Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request, 'Director eliminado con éxito')
    return redirect('director')
#Editar Director
def editarDirector(request,id):
    directorEditar = Director.objects.get(id=id)
    return render(request, 'editarDirector.html', {'directorEditar':directorEditar})
#Actualizando datos Director
def procesarActualizacionDirector(request):
    id=request.POST['id']
    dni=request.POST['dni']
    apellido=request.POST['apellido']
    nombre=request.POST['nombre']
    foto=request.FILES.get("foto")
    directorConsultado=Director.objects.get(id=id)
    directorConsultado.dni=dni
    directorConsultado.nombre=nombre
    directorConsultado.apellido=apellido
    directorConsultado.foto=foto
    directorConsultado.save()
    messages.success(request, 'Director actualizado con éxito')
    return redirect('listadoDirectores')

#---------------------Gestionar crud cine------------------------------------------------
def gestionCines(request):
    return render(request,'gestionCines.html')
#guardar cines
def guardarCine(request):
    nom=request.POST['nombre']
    dir=request.POST['direccion']
    tel=request.POST['telefono']
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel)
    return JsonResponse({
        'estado': True,
        'mensaje': 'Cine registrado existosamente'
    })

#Renderiras el listado Cines
def listadoCines(request):
    cines=Cine.objects.all()
    return render(request,'listadoCines.html',{'cines':cines})

#--------------------------Director fetch-----------------------
def director(request):
    return render(request,'director.html')

def listaDirector(request):
    directores=Director.objects.all()
    return render(request,'listaDirector.html',{'directores':directores})

#Guardar Director
def guardarDirector(request):
    dni=request.POST['dni']
    nom=request.POST['nombre']
    ape=request.POST['apellido']
    fot=request.FILES.get("foto")
    nuevoDirector=Director.objects.create(dni=dni,nombre=nom,apellido=ape,foto=fot)
    return JsonResponse({'estado': True, 'mensaje': 'Director guardado correctamente'})

#--------------------------Pelicula fetch-----------------------------
def pelicula(request):
    return render(request,'pelicula.html')

def listaPelicula(request):
    peliculas=Pelicula.objects.all()
    return render(request,'listaPelicula.html',{'peliculas':peliculas})

#Nuevo Pelicula


#Guardar Pelicula
def guardarPelicula(request):
    if request.method == 'POST':
        tit = request.POST['titulo']
        dura = request.POST['duracion']
        sin = request.POST['sinopsis']
        genero_id = request.POST["genero"]
        director_id = request.POST["director"]
        genero = Genero.objects.get(id=genero_id)
        director = Director.objects.get(id=director_id)
        nueva_pelicula = Pelicula.objects.create(titulo=tit, duracion=dura, sinopsis=sin, genero=genero, director=director)
        return JsonResponse({'estado': True, 'mensaje': 'Pelicula guardada correctamente'})

    generosBdd = Genero.objects.all()
    directores = Director.objects.all()
    return render(request, 'pelicula.html', {'generos': generosBdd, 'directores': directores})

