from django.urls import path
from . import views

urlpatterns = [
    path('tipos/', views.carreras_type, name='carreras_type'),
    path('tipos/editar/<int:id>/', views.carreras_type_edit, name='carreras_type_edit'),
    path('tipos/eliminar/<int:id>/', views.carreras_type_delete, name='carreras_type_delete'),
]