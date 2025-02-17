from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #para pedir login e evitar acesso não autorizado
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
import logging
from django.contrib import messages
from ..models import Usuario , Produto
from django.contrib.auth.hashers import check_password
import datetime


### função de login da pagina
###### erro nessa merda aqui kjkjkjkkjkjkjkjkjkjkkjkjkjkj
## eu quero que a segurança da aplicação vai toma no cu
## qualquer um vai acessar tudo no site, ate o banco de dados e mudar os dados nessa poha
## django n quer facilitar nessa poha
## eu tambem tenho que fazer tudo nessa poha, banco de dados, segurança
## frontend, backend, testar, aprovar, to cansado pra crlh
def login(request):
    if request.method == 'POST':
        usuario = request.POST.get('email')
        senha = request.POST.get('senha')
        logging.info(f'Tentativa de login com usuário {usuario}')
        print(usuario, senha)
        try:
            autentic = Usuario.objects.filter(username=usuario).first()
            if senha == autentic.password:
                request.session['user_id'] = autentic.idusuario
                #login(request, autentic)
                return redirect('home')
            else:
                print('Erro ao autenticae')
                return messages.error(request,'Erro ao autenticar')
        except:
            print('Erro no try')
            return messages.error(request,'Erro no server')
    return render(request, 'login/login.html')

### função do menu principal da aplicação
####
def home(request):
    contexto = {}
    hora = datetime.datetime.now().strftime('%H:%M')
    contexto['hora'] = hora
    return render(request, 'menus/home.html',contexto)

### função do menu do estoque
#####
def estoque(request):
    produtos = Produto.objects.all()
    contexto = {'produtos': produtos}
    return render(request, 'estoque/estoque.html', contexto)

### função de deletar produto, mas não tem html
#####
def deletarProduto(request):
    if request.method == 'POST':
        idproduto = request.POST.get('idprodutodelete')
        print(idproduto)
        if idproduto:
            produto = Produto.objects.filter(idproduto=idproduto).first()
            produto.delete()
            messages.success(request, 'Removido com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro em deletar dados')
    else:
        messages.error(request, 'methodo não permitido')
        return redirect('estoque')

### função de ver o dados completo do produto
#####
def descricaoProduto(request):
    idproduto = request.POST.get('idprodutodescricao')
    descricao = Produto.objects.filter(idproduto=idproduto).first()
    contexto = {'descricao': descricao}
    return render(request, 'estoque/descricao.html',contexto)

### função de editar o produto
######
def editarProduto(request):
    if request.method == 'POST':
        idproduto = request.POST.get('idprodutoeditar')
        if idproduto:
            produto = get_object_or_404(Produto, idproduto=idproduto)
            produto.preco = request.form.get('precoi')
            produto.descricao = request.form.get('descricaoi')
            produto.quantidade = request.form.get('quantidadei')
            produto.controlado = request.form.get('controladoi')
            produto.save()
            return redirect('estoque')
    dadosprodutos = Produto.objects.filter(idproduto=idproduto).first()
    dados = {'dados': dadosprodutos}
    return render(request, 'estoque/editar.html', dados)

### função de adicionar produtos
#########
def adicionarProdutos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        controlado = request.POST.get('controlado')
        try:
            produtoNovo = Produto(
                nome=nome,
                descricao=descricao,
                preco=preco,
                quantidade=quantidade,
                controlado=controlado)
            produtoNovo.save()
            messages.success(request, 'Produto adicionado com sucesso!')  
            return redirect('estoque')
        except:
            return messages.error(request, 'Erro ao adicionar')
    return render(request, 'estoque/adicionar.html')