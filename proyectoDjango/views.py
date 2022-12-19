from django.http import HttpResponse
import datetime

def HolaMundo(request): #primera vista

    documento="""<html>
    <body>
    <h1>
    Hola mundo
    </html>
    </body>
    </h1>"""

    return HttpResponse(documento)

def fecha(request):
    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" %fecha_actual

    return HttpResponse(documento)

def calculoEdad(request, edad, year):    
    edadFutura=edad+year
    yearFuturo= 2023+year
    documento="""<html>
    <head>
    <title>
       Calculo edad
    </title>
    </head>
    <body>
        <h1>En el año %s tendrás %s años</h1>
    </body>
    </html>""" %(yearFuturo,edadFutura)
    
    return HttpResponse(documento)