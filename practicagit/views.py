from django.http import HttpResponse
from django.template import Context,Template,loader
from base.models import Alumno


def ver_alumno (request):
    alumno1=Alumno(nombre='Julian',apellido='Alvear',edad=24)
    alumno2=Alumno(nombre='Pedro',apellido='Alvear',edad=94)
    alumno1.save()
    alumno2.save()
    alumnos=Alumno.objects.all()
    template=loader.get_template('ver_alumno.html')
    template_renderizado=template.render({'alumnos':alumnos})
    return HttpResponse(template_renderizado)