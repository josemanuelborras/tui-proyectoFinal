from django.urls import path
from . import views

from carrera import views as carrera_views
from materia import views as materia_views
from alumnos import views as alumnos_views

urlpatterns = [
    path('login/', views.login_view, name='admin_login'),
    path('', views.admin_home, name='admin_home'),
    path('logout/', views.logout_view, name='admin_logout'),
    # Carreras
    path('carreras/', carrera_views.carreras_list, name='carreras_list'),
    # Tipos de Carreras
    path('carrerasType/', carrera_views.carreras_type, name='carreras_type'),

    path('tipos/', carrera_views.carreras_type, name='carreras_type'),
    path('tipos/editar/<int:id>/', carrera_views.carreras_type_edit, name='carreras_type_edit'),
    path('tipos/eliminar/<int:id>/', carrera_views.carreras_type_delete, name='carreras_type_delete'),
    path('carreras/crear/', carrera_views.carrera_create, name='carrera_create'),
    path('carreras/editar/<int:id>/', carrera_views.carrera_edit, name='carrera_edit'),
    path('carreras/eliminar/<int:id>/', carrera_views.carrera_delete, name='carrera_delete'),
    path('carrera/<int:carrera_id>/', carrera_views.carrera_detail, name='carrera_detail'),
    path('carrera/<int:carrera_id>/agregar-materia/', carrera_views.carrera_agregar_materia, name='carrera_agregar_materia'),
    path('carrera/<int:carrera_id>/quitar-materia/<int:materia_id>/', carrera_views.carrera_quitar_materia, name='carrera_quitar_materia'),

    # Materias
    path('materias/', materia_views.materias_list, name='materias_list'),
    path('materias/crear/', materia_views.materia_create, name='materia_create'),
    path('eliminar/<int:materia_id>/', materia_views.materia_delete, name='materia_delete'),
    path('editar/<int:materia_id>/', materia_views.materia_edit, name='materia_edit'),
    # Alumnos
    path('alumnos/', alumnos_views.alumnos_list, name='alumnos_list'),
    path('alumnos/eliminar/<int:alumno_id>/', alumnos_views.alumno_delete, name='alumno_delete'),
]