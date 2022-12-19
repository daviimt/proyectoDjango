from django.http import HttpResponse
import datetime
from django.template import Template, Context

def HolaMundo(request): #primera vista

    doc_externo=open("C:/Users/ruben/OneDrive/Escritorio/2DAM/PSP/UD4/proyectoDjango/proyectoDjango/plantillas/holamundo.html")

    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context()
    documento=plt.render(ctx)
    
    return HttpResponse(documento)

def fecha(request):
    fecha_actual=datetime.datetime.now()

    doc_externo=open("C:/Users/ruben/OneDrive/Escritorio/2DAM/PSP/UD4/proyectoDjango/proyectoDjango/plantillas/fecha.html")

    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context({"ahora":fecha_actual})
    documento=plt.render(ctx)

    return HttpResponse(documento)

def calculoEdad(request, edad, year):    
    edadFutura=edad+year
    yearFuturo= 2023+year

    doc_externo=open("C:/Users/ruben/OneDrive/Escritorio/2DAM/PSP/UD4/proyectoDjango/proyectoDjango/plantillas/calcularEdad.html")

    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context({"proximaEdad":edadFutura, "proximoYear":yearFuturo})

    documento=plt.render(ctx)

    return HttpResponse(documento)
    
    