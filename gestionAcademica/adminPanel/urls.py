from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='admin_login'),
    path('', views.admin_home, name='admin_home'),
]