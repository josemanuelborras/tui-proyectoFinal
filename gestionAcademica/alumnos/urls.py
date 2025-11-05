from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.alumno_login, name='alumno_login'),
    path('panel/', views.alumno_main, name='alumnos_main'),
    path('carrera/<int:carrera_id>/', views.alumno_carrera_detail, name='alumno_carrera_detail'),
    path('logout/', views.alumno_logout, name='alumno_logout'),
    path('carrera/<int:carrera_id>/inscribir-materia/<int:materia_id>/', views.alumno_inscribir_materia, name='alumno_inscribir_materia'),
    path('carrera/<int:carrera_id>/comprobante-materia/<int:materia_id>/', views.alumno_comprobante_materia, name='alumno_comprobante_materia'),
]