from django.urls import path

from control.views import teams, league, sudamericana, equipos_clasificados, buscar_equipos

urlpatterns = [
    path('equipos_libertadores/', teams, name="equipos_libertadores"),
    path('equipo-CL/', league, name="equipos_champions"),
    path('equipos_sudamericana', sudamericana, name='equipos_sudamericana'),
    path('lista/', equipos_clasificados, name='lista'),
    path('buscar_equipos/', buscar_equipos, name='buscar_equipos',)
]

