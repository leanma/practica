from django.urls import path
from base import views

urlpatterns = [
    path('',views.inicio),
    path('cursos',views.cursos),
    path('ver-alumno/', views.ver_alumno)
]
