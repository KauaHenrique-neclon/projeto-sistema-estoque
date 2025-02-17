from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from ..models import Usuario


def index(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        try:
            novoUsuario = Usuario(
                username = nome,
                password = senha
            )
            novoUsuario.save()
            return messages.success(request, 'Usuario criado')
        except:
            return messages.error(request, 'Erro ao criar um usuario')
    dadosUsuario = Usuario.objects.all()
    contexto = {'usuario':dadosUsuario}
    return render(request, 'usuario/usuario.html', contexto)