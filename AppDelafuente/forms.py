from django import forms

class CursoFormulario(forms.Form):
    
    curso = forms.CharField()
    comision = forms.IntegerField()
    
class EstudianteFormulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField() 
    edad = forms.IntegerField()
    
class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
    
class EntregableFormulario(forms.Form):
    nombre = forms.CharField()
    fechaEntrega = forms.DateField()
    entregado = forms.BooleanField()