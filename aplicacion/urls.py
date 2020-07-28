from django.urls import path
from aplicacion import views

urlpatterns = [
    path('', views.home, name="home"),
    path('servicio/', views.servicio, name="servicio"),
    path('listar_pelicula/', views.listar_pelicula, name="listar_peli"),
    path('registrar_pelicula/', views.registrar_pelicula, name="registrar_peli"),
    path('modificar_pelicula/<id>/', views.modificar_pelicula, name="modificar_peli"),
    path('eliminar_pelicula/<id>/', views.eliminar_pelicula, name="eliminar_peli"),
    path('registro/', views.registrar_usuario, name="registrar_usuario")
]