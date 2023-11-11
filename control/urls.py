from django.urls import path

from control.views import teams, league, sudamericana, equipos_clasificados, buscar_equipos

urlpatterns = [
    path('teams-squad/', teams, name="equipos_libertadores"),
    path('equipo-CL/', league, name="equipos_champions"),
    path('equipos_sudamericana', sudamericana, name='equipos_sudamericana'),
    path('cupos/', equipos_clasificados, name='lista'),
    path('buscar_equipos/', buscar_equipos, name='buscar_equipos',)
]

