
from django.urls import path
from . import views
from django.conf.urls import handler404
from Aplicaciones.qr.views import error_404_view

app_name= 'gestion'
urlpatterns = [
    path('', views.home, name='dashboard'),
    path("crear_evento/", views.crear_evento, name="crear_evento"),
    path("autent_qr/", views.autent_qr, name="autent_qr"),
    path("Inscripciones/", views.Inscripciones, name="Inscripciones"),
    path("event_creado/", views.event_creado, name="event_creado"),
    path("charts/", views.charts, name="charts"),

    path('administrador/logout/', views.signout, name='logout'),
    path('administrador/signin/', views.signin, name='signin'),
    path('administrador/registrar/', views.registrar),
    path('administrador/editar/', views.editar),
    path('administrador/edicion/<custom_id>', views.edicion),
    path('administrador/eliminar/<custom_id>', views.eliminar),
    path('user/<custom_id>', views.datos),
]