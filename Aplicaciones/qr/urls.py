from django.urls import path
from . import views
# from django.conf.urls import handler404
# from Aplicaciones.qr.views import error_404_view

app_name = 'gestion'
urlpatterns = [

    # Dominio principal de la aplicacion
    path('', views.home, name='home'),


    # Modulo de autenticacion
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),

    # Modulo de administracion
    path('administrador/dashboard/', views.dashboard),
    path('administrador/registrar/', views.registrar),
    path('administrador/editar/', views.editar),
    path('administrador/edicion/<id>', views.edicion),
    path('administrador/eliminar/<id>', views.eliminar),


    # Modulo de usuarios
    path('user/<id>', views.datos),
]
