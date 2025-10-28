from django.urls import path
from . import views

urlpatterns = [
  path('inscripcion/', views.inscripcion_carrera, name='inscripcion_carrera'),
  path('inscripcion/<int:alumno_id>/<int:carrera_id>/', views.inscripcion_materias_view, name='inscripcion_materias'),

]

