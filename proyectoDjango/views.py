from django.http import HttpResponse

def HolaMundo(request): #primera vista
    return HttpResponse("Hola Mundo")