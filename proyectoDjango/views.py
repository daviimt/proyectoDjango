from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.template import loader
from django.shortcuts import render 

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def HolaProfesor(request):

    p1=Persona("Rafa","Montero")
    ahora=datetime.datetime.now()
    lista=["Python","Java","Flutter","PHP","HTML"]
    return render(request, 'holaprofesor.html',{"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "lenguajes":lista})

def Trabajo(request):

    nombre1="Ruben"
    nombre2="Marta"
    nombre3="David"
    ahora=datetime.datetime.now()
    return render(request, 'trabajo.html',{"nombre_componente1":nombre1, "nombre_componente2":nombre2, "nombre_componente3":nombre3, "momento":ahora})


def HolaMundo(request): #primera vista
    doc_externo=loader.get_template('holamundo.html')

    documento=doc_externo.render()
    
    return HttpResponse(documento)

def fecha(request):
    fecha_actual=datetime.datetime.now()

    doc_externo=loader.get_template('fecha.html')

    ctx=Context({"ahora":fecha_actual})

    documento=doc_externo.render()

    return HttpResponse(documento)

def calculoEdad(request, edad, year):    
    edadFutura=edad+year
    yearFuturo= 2023+year

    doc_externo=loader.get_template('calcularEdad.html')

    documento=doc_externo.render({"proximaEdad":edadFutura, "proximoYear":yearFuturo})

    return HttpResponse(documento)
    
    