from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrar/', views.registrar),
    path('editar/<name>', views.editar),
    path('edicion/', views.edicion),
    path('eliminar/<cedula>', views.eliminar)
]