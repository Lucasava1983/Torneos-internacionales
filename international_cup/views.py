from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

def teams_html(request):
    contexto = {
        "local" : "Fluminense",
        "visitante" : "Boca Juniors"
    }

    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )

    return http_response