from django.urls import path

from control.views import teams

urlpatterns = [
    path('teams-squad/', teams),
]