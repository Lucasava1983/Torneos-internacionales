from django.shortcuts import render

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

def sudamericana(request):
    http_response = render(
        request=request,
        template_name='control/form_sudamericana.html',
        
    )

    return http_response