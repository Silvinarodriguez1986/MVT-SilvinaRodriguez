from multiprocessing import context
from unittest import loader
from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.template import Template, Context
from familia.models import Familia 
from django.template import loader
from datetime import datetime


def hello_world(request): 
    return HttpResponse("Hola esta es mi familia")

def title(request): 
    return HttpResponse("<h1>Estos son los miembros de mi familia</h1>")    

def her_name_is(request, nombre, edad): 
    documentoDeTexto = f"Su nombre es: <br><br> {nombre} <br><br> Su edad es: {edad}"
    return HttpResponse(documentoDeTexto)

def my_template(request):
    my_html = open('C:/Users/Silvina/desktop/mi_primer_mvt/mi_primer_mvt/mi_mvt/familia/templates/template.html')   
   
    template = Template(
        my_html.read()
        .encode("latin-1")
        .decode("utf-8")
        )

    my_html.close()
                                  
    context_dict = {
      
        "my_string": "Patricia Analia Miguel Walter Indira Iciar".split(),
        
        "nombre": "Patricia",
        "apellido": "De la camara",
        "relacion": "Mama",
        "edad": "65",

        }


    context = Context(
        context_dict
    )

    render = template.render(context) 

    return HttpResponse(render)

def count(request):
    documentoDeTexto = f"Tenemos cargados {Familia.objects.all().count()} familiares"
    return HttpResponse(documentoDeTexto)    

#def template_loader(request, nombre: str, apellido: str, relacion: str, nacimiento: str, edad: int):  

    template = loader.get_template("template_loader.html")  
    
    edad, nacimiento = calculate_age(nacimiento)  

    familia = Familia(
        nombre=nombre, apellido=apellido, relacion=relacion, nacimiento=nacimiento, edad=edad 
    )

    familia.save() 


    context_dict = {"miembro": familia}
    render = template.render(context_dict)
    return HttpResponse(render)

def familia(request):
    familia = Familia.objects.all()

    context_dict = {"familia": familia} 
    return render(
          request=request,
        context=context_dict,
        template_name="familia/template.html",
    )

def calculate_age(nacimiento: str) -> int:
    nacimiento = datetime.strptime(nacimiento, "%Y-%m-%d")
    delta_time = datetime.now() - nacimiento
    days_by_year = 365.25

    years=int(delta_time.days // days_by_year)
    return years, nacimiento

  