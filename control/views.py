from django.shortcuts import render

# Create your views here.
def teams(request):
    contexto = {
        "local" : "Fluminense",
        "visitante" : "Boca Juniors"
    }

    http_response = render(
        request=request,
        template_name='equipos.html',
        context=contexto,
    )

    return http_response