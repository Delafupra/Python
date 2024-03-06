from django.shortcuts import render
from django.http import HttpResponse
from AppDelafuente.models import *
from AppDelafuente.forms import *


# Create your views here.

def inicio(request):

    return render(request, "AppDelafuente/inicio.html")


def estudiantes(request):

    return render(request, "AppDelafuente/estudiantes.html")

def cursos(request):

    return render(request, "AppDelafuente/cursos.html")

def profesores(request):

    return render(request, "AppDelafuente/profesores.html")

def entregables(request):

    return render(request, "AppDelafuente/entregables.html")

def cursoFormulario(request):
    
    if request.method == "POST": #despues de dar click al boton enviar
        
        formulario1 = CursoFormulario(request.POST)
        
        if formulario1.is_valid():
            
            info = formulario1.cleaned_data
            
            curso = Curso(nombre=info["curso"], comision=info["comision"]) #nombre viene de models y curso de html

            curso.save()
        
            return render(request, "AppDelafuente/cursos.html")
        
    else:
        
        formulario1 = CursoFormulario()
    
    return render(request, "AppDelafuente/cursoFormulario.html", {"form1":formulario1})


def busquedaComision(request):
    
    return render(request, "AppDelafuente/cursos.html")

def resultados(request):
    
    if request.GET["comision"]:
        
        comision =request.GET["comision"]
        cursos = Curso.objects.filter(comision__iexact=comision)
        
        return render(request, "AppDelafuente/inicio.html", {"cursos":cursos, "comision":comision})
    
    else:
        
        respuesta = "No enviaste datos"
    
    
    return HttpResponse(respuesta)


def estudianteFormulario(request):
    
    if request.method == "POST": #despues de dar click al boton enviar
        
        formulario2 = EstudianteFormulario(request.POST)
        
        if formulario2.is_valid():
            
            info = formulario2.cleaned_data
            
            estudiante = Estudiante(nombre=info["nombre"], apellido=info["apellido"], edad=info["edad"], email=info["email"] ) #nombre viene de models y curso de html

            estudiante.save()
        
            return render(request, "AppDelafuente/estudiantes.html")
        
    else:
        
        formulario2 = EstudianteFormulario()
    
    return render(request, "AppDelafuente/estudianteFormulario.html", {"form2":formulario2})

def busquedaNombre(request):
    
    return render(request, "AppDelafuente/estudiantes.html")

def resultados1(request):
    
    if request.GET["nombre"]:
        
        nombre =request.GET["nombre"]
        estudiantes = Estudiante.objects.filter(nombre__iexact=nombre)
        
        return render(request, "AppDelafuente/estudiantes.html", {"nombre":nombre, "estudiantes":estudiantes})
    
    else:
        
        respuesta = "No enviaste datos"
    
    
    return HttpResponse(respuesta)


def profesorFormulario(request):
    
    if request.method == "POST": #despues de dar click al boton enviar
        
        formulario3 = ProfesorFormulario(request.POST)
        
        if formulario3.is_valid():
            
            info = formulario3.cleaned_data
            
            profesor = Profesor(nombre=info["nombre"], apellido=info["apellido"], profesion=info["profesion"], email=info["email"] ) #nombre viene de models y curso de html

            profesor.save()
        
            return render(request, "AppDelafuente/profesores.html")
        
    else:
        
        formulario3 = ProfesorFormulario()
    
    return render(request, "AppDelafuente/profesorFormulario.html", {"form3":formulario3})

def busquedaNombreProfe(request):
    
    return render(request, "AppDelafuente/profesores.html")

def resultados2(request):
    
    if request.GET["nombre"]:
        
        nombre =request.GET["nombre"]
        profesores = Profesor.objects.filter(nombre__iexact=nombre)
        
        return render(request, "AppDelafuente/profesores.html", {"nombre":nombre, "profesores":profesores})
    
    else:
        
        respuesta = "No enviaste datos"
    
    
    return HttpResponse(respuesta)


def entregableFormulario(request):
    
    if request.method == "POST": #despues de dar click al boton enviar
        
        formulario4 = EntregableFormulario(request.POST)
        
        if formulario4.is_valid():
            
            info = formulario4.cleaned_data
            
            entregable = Entregable(nombre=info["nombre"], fechaEntrega=info["fechaEntrega"], entregado=info["entregado"], ) #nombre viene de models y curso de html

            entregable.save()
        
            return render(request, "AppDelafuente/entregables.html")
        
    else:
        
        formulario4 = EntregableFormulario()
    
    return render(request, "AppDelafuente/entregableFormulario.html", {"form4":formulario4})

def busquedaNombreEntregable(request):
    
    return render(request, "AppDelafuente/profesores.html")

def resultados3(request):
    
    if request.GET["nombre"]:
        
        nombre =request.GET["nombre"]
        entregables = Entregable.objects.filter(nombre__iexact=nombre)
        
        return render(request, "AppDelafuente/entregables.html", {"nombre":nombre, "entregables":entregables})
    
    else:
        
        respuesta = "No enviaste datos"
    
    
    return HttpResponse(respuesta)
