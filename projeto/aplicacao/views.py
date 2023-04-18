from django.shortcuts import render
from .models import Aplicacao, Lista

# Create your views here.

def index(request):
    return render(request, "aplicacao/index.html", {
        "aplicacao": Aplicacao.objects.all()
    })


def aplicacao(request, aplicacao_id):
    compra = Aplicacao.objects.get(id=aplicacao_id)
  
    return render(request, "aplicacao/pag.html", {
        "Aplicacao": compra,
        "Aplicacao": aplicacao

      
    })