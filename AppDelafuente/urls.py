
from django.urls import path
from AppDelafuente.views import  *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("cursos", cursos, name="Cursos"),
    path("estudiantes", estudiantes, name="Estudiantes"),
    path("profesores", profesores, name="Profesores"),
    path("entregables", entregables, name="Entregables"),
    path("cursoFormulario", cursoFormulario, name="FormularioCurso"),
    path("buscarComision", busquedaComision, name="BuscarComision"),
    path("resultados", resultados, name="ResultadosBusqueda"),
    path("estudianteFormulario", estudianteFormulario, name="FormularioEstudiante"),
    path("buscarNombre", busquedaNombre, name="BuscarNombre"),
    path("resultados1", resultados1, name="ResultadosBusqueda1"),
    path("profesorFormulario", profesorFormulario, name="FormularioProfesor"),
    path("buscarNombreProfe", busquedaNombreProfe, name="BuscarNombreProfe"),
    path("resultados2", resultados2, name="ResultadosBusqueda2"),
    path("entregableFormulario", entregableFormulario, name="FormularioEntregable"),
    path("buscarNombreEntregable", busquedaNombreEntregable, name="BuscarNombreEntregable"),
    path("resultados3", resultados3, name="ResultadosBusqueda3"),
]
