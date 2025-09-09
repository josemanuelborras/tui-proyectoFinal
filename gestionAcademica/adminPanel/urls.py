from django.urls import path
from . import views

from carrera import views as carrera_views

urlpatterns = [
    path('login/', views.login_view, name='admin_login'),
    path('', views.admin_home, name='admin_home'),
    path('logout/', views.logout_view, name='admin_logout'),
    path('carreras/', carrera_views.carreras_list, name='carreras_list'),
    path('carrerasType/', carrera_views.carreras_type, name='carreras_type'),
]