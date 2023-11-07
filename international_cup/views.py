from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

def semifinal(request):
    contexto = {}
    http_response = render(
        request=request
        
    )