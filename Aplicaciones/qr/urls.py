from django.urls import path
from . import views

app_name= 'gestion'
urlpatterns = [
    path('', views.home),
    path('administrador/signup/', views.signup, name='signup'),
    path('administrador/logout/', views.signout, name='logout'),
    path('administrador/signin/', views.signin, name='signin'),
    path('administrador/registrar/', views.registrar),
    path('administrador/editar/', views.editar),
    path('administrador/edicion/<custom_id>', views.edicion),
    path('administrador/eliminar/<custom_id>', views.eliminar),
    path('user/<custom_id>', views.datos),
]