from django.urls import path
from . import views

urlpatterns = [
    path('tipos/', views.carreras_type, name='carreras_type'),
    path('tipos/editar/<int:id>/', views.carreras_type_edit, name='carreras_type_edit'),
    path('tipos/eliminar/<int:id>/', views.carreras_type_delete, name='carreras_type_delete'),
    path('carreras/crear/', views.carrera_create, name='carrera_create'),
    path('carreras/editar/<int:id>/', views.carrera_edit, name='carrera_edit'),
    path('carreras/eliminar/<int:id>/', views.carrera_delete, name='carrera_delete'),
    path('carrera/<int:carrera_id>/', views.carrera_detail, name='carrera_detail'),
    path('carrera/<int:carrera_id>/agregar-materia/', views.carrera_agregar_materia, name='carrera_agregar_materia'),
    path('carrera/<int:carrera_id>/quitar-materia/<int:materia_id>/', views.carrera_quitar_materia, name='carrera_quitar_materia'),
]