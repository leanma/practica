from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context,Template,loader
from base.models import Alumno
from django.shortcuts import render

def inicio(request):
    return HttpResponse('vista inicio')

def cursos(request):
    template=loader.get_template('cursos.html')
    template_renderizado=template.render()
    return HttpResponse(template_renderizado)


def ver_alumno (request):
    alumno1=Alumno(nombre='Julian',apellido='Alvear',edad=24)
    alumno2=Alumno(nombre='Pedro',apellido='Alvear',edad=94)
    alumno1.save()
    alumno2.save()
    alumnos=Alumno.objects.all()
    return render(request,"base/ver_alumno.html",{'alumnos':alumnos})
