from django.shortcuts import render

from control.models import Copa_Libertadores

# Create your views here.
def teams(request):
    contexto = {
        "visitante" : Copa_Libertadores.objects.all()
    }

    http_response = render(
        request=request,
        template_name='control/equipos.html',
        context=contexto,
    )

    return http_response