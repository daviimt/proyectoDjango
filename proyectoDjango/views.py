from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def HolaProfesor(request):

    p1=Persona("Rafa","Montero")
    ahora=datetime.datetime.now()

    doc_externo=open("proyectoDjango\plantillas\html\holaprofesor.html")

    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido})
    documento=plt.render(ctx)
    
    return HttpResponse(documento)

def Trabajo(request):

    nombre1="Ruben"
    nombre2="Marta"
    nombre3="David"
    ahora=datetime.datetime.now()

    doc_externo=open("proyectoDjango\plantillas\html\trabajo.html")

    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context({"nombre_componente1":nombre1, "nombre_componente2":nombre2, "nombre_componente3":nombre3, "momento":ahora})
    documento=plt.render(ctx)
    
    return HttpResponse(documento)

def HolaMundo(request): #primera vista
    doc_externo=open("proyectoDjango\plantillas\html\holamundo.html")

    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context()
    documento=plt.render(ctx)
    
    return HttpResponse(documento)

def fecha(request):
    fecha_actual=datetime.datetime.now()

    doc_externo=open("proyectoDjango\plantillas\html\\fecha.html")

    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context({"ahora":fecha_actual})
    documento=plt.render(ctx)

    return HttpResponse(documento)

def calculoEdad(request, edad, year):    
    edadFutura=edad+year
    yearFuturo= 2023+year

    doc_externo=open("proyectoDjango\plantillas\html\calcularEdad.html")

    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context({"proximaEdad":edadFutura, "proximoYear":yearFuturo})

    documento=plt.render(ctx)

    return HttpResponse(documento)
    
    