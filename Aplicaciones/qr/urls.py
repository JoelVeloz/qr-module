from django.urls import path
from . import views

urlpatterns = [
    path('administrador/', views.home),
    path('administrador/registrar/', views.registrar),
    path('administrador/editar/', views.editar),
    path('administrador/edicion/<cedula>', views.edicion),
    path('administrador/eliminar/<cedula>', views.eliminar)
]