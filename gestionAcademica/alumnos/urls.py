from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.alumno_login, name='alumno_login'),
    path('panel/', views.alumno_panel, name='alumno_panel'),
    path('logout/', views.alumno_logout, name='alumno_logout'),
]