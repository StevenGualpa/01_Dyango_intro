from urllib import response
from django.http import HttpResponse

def saludo(response):
    return HttpResponse("Primera Pagina en Dyang :v")

def despedida(response):
    return HttpResponse("NOs vemos mánana")

def saludo02(response)