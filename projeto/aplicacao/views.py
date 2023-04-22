from django.shortcuts import render
from .models import Aplicacao, Lista
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'aplicacao/inicio.html')



def index(request):
    return render(request, "aplicacao/index.html", {
        "aplicacao": Aplicacao.objects.all()
    })




def aplicacao(request, aplicacao_id):
    compra = Aplicacao.objects.get(id=aplicacao_id)
  
    return render(request, "aplicacao/pag.html", {
        "aplicacao": compra,

      
    })




def cadastro(request):
    if request.method == 'GET':
        return render(request, 'aplicacao/cadastro.html')
    
    else:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        usuario = User.objects.filter(username=nome).first()
        if usuario:
            return HttpResponse(f'Usuário ja existe {nome}')
        
        usuario = User.objects.create_user(username=nome, password=senha)
        usuario.save()
        return HttpResponse(f'Usuário {nome} salvo com sucesso')
    

def logar(request):
    if request.method == 'GET':
        return render(request, 'aplicacao/logar.html')
    
    else:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        usuario = authenticate(username=nome, password=senha)

        if usuario:
            login(request, usuario)
            return HttpResponse('Usuario autenticado')
        

        else:
            return HttpResponse('Login ou Senha invalidos')
        

@login_required(login_url='/logar')
def pagina(request):
    return HttpResponse('Página...')