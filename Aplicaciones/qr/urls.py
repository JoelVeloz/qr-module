from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrar/', views.registrar),
    path('editar/', views.editar),
    path('edicion/<name>', views.edicion),
    path('eliminar/<cedula>', views.eliminar)
]