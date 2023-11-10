from django.urls import path

from control.views import teams, league, sudamericana

urlpatterns = [
    path('teams-squad/', teams, name="equipos_libertadores"),
    path('equipo-CL/', league, name="equipos_champions"),
    path('crear-equipo', sudamericana, name='crear_equipo'),
]