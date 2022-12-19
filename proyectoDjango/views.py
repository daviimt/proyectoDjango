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