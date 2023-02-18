from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('administrador/signup/', views.signup, name='signup'),
    path('administrador/logout/', views.signout, name='logout'),
    path('administrador/signin/', views.signin, name='signin'),
    path('administrador/registrar/', views.registrar),
    path('administrador/editar/', views.editar),
    path('administrador/edicion/<cedula>', views.edicion),
    path('administrador/eliminar/<cedula>', views.eliminar),
    path('user/<cedula>', views.datos)
]