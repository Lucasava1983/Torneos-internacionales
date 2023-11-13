from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from control.forms import CuposSudamericana
from control.models import Copa_Libertadores, Copa_Sudamericana, Champions_League

# Create your views here.
def teams(request):
    contexto = {
        "visitante" : Copa_Libertadores.objects.all(),
    }

    http_response = render(
        request=request,
        template_name='control/equipos.html',
        context=contexto,
    )

    return http_response



def league(request):
    contexto = {
        "visitante" : Champions_League.objects.all(),
    }

    http_response = render(
        request=request,
        template_name='control/league.html',
        context=contexto,
    )

    return http_response

def equipos_clasificados(request):
    contexto = {
        "cupos" : Copa_Sudamericana.objects.all(),
    }

    http_response = render(
        request=request,
        template_name='control/lista.html',
        context=contexto,
    )
    return http_response

def sudamericana_v1(request):
    if request.method == "POST":
        data = request.POST
        cupo = Copa_Sudamericana(equipo=data['equipo'], director_tecnico=data['tecnico'], capitan=data['jugador'], dorsal=data['dorsal'])
        cupo.save()
        url_list = reverse('lista')
        return redirect(url_list)
    else:
        http_response = render(
            request=request,
            template_name='control/form_sudamericana.html',
        
        )
        return http_response
    
def sudamericana(request):
    if request.method == "POST":
        formulario = CuposSudamericana(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            equipo = data["equipo"]
            director_tecnico = data["director_tecnico"]
            capitan = data["capitan"]
            dorsal = data["dorsal"]
            qualified = Copa_Sudamericana(equipo=equipo, director_tecnico=director_tecnico, capitan=capitan, dorsal=dorsal)
            qualified.save()
            url_successful = reverse('lista')
            return redirect(url_successful)
    else:
        formulario = CuposSudamericana()
    http_response = render(
        request=request,
        template_name='control/form_qualified.html',
        context={'formulario': formulario}
    )

    return http_response

def buscar_equipos(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]

        cupos = Copa_Sudamericana.objects.filter(
            Q(equipo__contains=busqueda) | Q(director_tecnico__contains=busqueda) | Q(capitan__contains=busqueda) | Q(dorsal__contains=busqueda)
            )
        contexto = {
            "cupos": cupos,
        }
        http_response = render(
            request=request,
            template_name='control/lista.html',
            context=contexto,
        )
        return http_response