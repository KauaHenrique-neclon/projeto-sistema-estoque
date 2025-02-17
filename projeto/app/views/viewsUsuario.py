from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from ..models import Usuario
import re


def index(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        padrão = r"^[a-zA-Z0-9._%+-]+@[gmail.-]+\.(com)$"
        if re.match(padrão, nome, re.IGNORECASE):
            if len(senha) >= 8 and senha.isdigit():    
                try:
                    novoUsuario = Usuario(
                        username = nome,
                        password = senha
                    )
                    novoUsuario.save()
                    return messages.success(request, 'Usuario criado')
                except:
                    return messages.error(request, 'Erro ao criar um usuario')
            else:
                return messages.error(request, 'Senha deve ter mais de 8 caracteres')
        else:
            return messages.error(request, 'Deve ser email')
    dadosUsuario = Usuario.objects.all()
    contexto = {'usuario':dadosUsuario}
    return render(request, 'usuario/usuario.html', contexto)