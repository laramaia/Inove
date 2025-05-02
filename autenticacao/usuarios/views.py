from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Perfil
from django.contrib.auth import authenticate, login
from .helpers import validar_email, validar_senha

def cadastro(request):
    if request.method == "GET": # Encaminhar para página de cadastro
        return render(request, 'cadastro.html')
    else: # Cliente já se cadastrou
        nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        tipo_usuario = request.POST.get('tipo_usuario')

        if User.objects.filter(email=email).exists():
            return HttpResponse('Esse e-mail já está cadastrado.')
        
        erro_email = validar_email(email)
        if erro_email:
            return HttpResponse(erro_email)
        
        erro_senha = validar_senha(senha)
        if erro_senha:
            return HttpResponse(erro_senha)
        
        user = User.objects.create_user(username=email, email=email, password=senha)
        user.first_name = nome_completo
        user.save()

        # cria perfil do usuário: professor ou estudante
        perfil = Perfil(user=user, tipo=tipo_usuario)
        perfil.save()
  
        return HttpResponse('Cadastro realizado com sucesso.')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username=email, password=senha)
        if user:
            login(request, user)
            perfil = Perfil.objects.get(user=user)
            
            if perfil.tipo == 'professor':
                return render(request, 'home_professor.html')
            else:
                return render(request, 'home_estudante.html')
        else:
            print("Login inválido.")