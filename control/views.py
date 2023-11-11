from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
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
        template_name='control/lista_clasificados.html',
        context=contexto,
    )

    return http_response

def sudamericana(request):
    if request.method == "POST":
        data = request.POST
        cupo = Copa_Sudamericana(nombre=data['nombre'], director_tecnico=data['tecnico'], capitan=data['jugador'], dorsal=data['dorsal'])
        cupo.save()
        url_exitosa = reverse('lista_clasificados') 
        return redirect(url_exitosa)
    else:
        http_response = render(
            request=request,
            template_name='control/form_sudamericana.html',
        )
        return http_response