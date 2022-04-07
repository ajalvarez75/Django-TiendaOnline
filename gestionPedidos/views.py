from email import message
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.forms import FormularioContacto
from gestionPedidos.models import Articulos
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def busqueda_productos(request):

    return render(request, 'busqueda.html')

def buscar(request):

    if request.GET["prd"]:

        #mensaje="Articulo buscado: %r" %request.GET["prd"]
        producto=request.GET["prd"]

        if len(producto)>20:

            mensaje="Texto de busqueda demasiado largo"

        else:

            articulos=Articulos.objects.filter(nombre__icontains=producto)
            #nombre__icontrains equivale a like nombre que se usa en busquedas de BD

            return render(request, "resultados.html", {"articulos":articulos, "query":producto})

    else:

        mensaje="por favor introduce un articulo a buscar"

    return HttpResponse(mensaje)

'''
primera forma de la funcion.

@csrf_exempt
def contacto(request):

    if request.method=="POST":

        subject=request.POST["asunto"]

        message=request.POST["mensaje"] + " " + request.POST["email"]

        email_from=settings.EMAIL_HOST_USER

        recipient_list=["ajac890602@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, "gracias.html")

    return render(request, "contacto.html")
    '''

@csrf_exempt
def contacto(request):

    if request.method=="POST":

        miFormulario=FormularioContacto(request.POST)

        if miFormulario.is_valid():

            infFrom=miFormulario.cleaned_data

            send_mail(infFrom['asunto'], infFrom['mensaje'], 
            infFrom.get('email',''),['ajac890602@gmail.com'],)

            return render(request, "gracias.html")

    else:

        miFormulario=FormularioContacto()

    return render(request, "formulario_contacto.html", {"form":miFormulario})
