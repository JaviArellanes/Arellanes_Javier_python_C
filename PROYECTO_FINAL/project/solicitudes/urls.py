from django.urls import path
from . import views

urlpatterns = [
    #path('', views.inicio, name="index"),
    #path('login', views.login, name="login"), 
    path('ver-solicitudes', views.Ver.as_view(), name="ver"), 
    path('crear-solicitud', views.crear.as_view(), name="crear"), 
    #path('insertar_solicitud', views.insertar_solicitud, name="insertar")
    path('index', views.inicio, name='index'),
    path('base', views.base, name= 'base'),
    path('eliminar-solicitud/<int:solicitud_id>/', views.eliminarSolicitud.as_view(), name='eliminar-solicitud')
]