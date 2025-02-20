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
    produtos = Produto.objects.all(is_active=True)
    contexto = {'produtos': produtos}
    return render(request, 'estoque/estoque.html', contexto)

### função de deixar falso o produto, mas não tem html
#####
def deletarProduto(request):
    if request.method == 'POST':
        idproduto = request.POST.get('idprodutodelete')
        if idproduto:
            isDesativar = Produto(
                idproduto = idproduto,
                is_active = False
            )
            isDesativar.save()
            messages.success(request, 'Removido com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro em desativar produto')
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
    idproduto = request.POST.get('idprodutoeditar')
    if request.method == 'POST':
        idDoProduto = request.POST.get('dadosIdProduto')
        if idDoProduto:
            descricao = request.POST.get('descricaoi')
            preco = request.POST.get('precoi')
            quantidade = request.POST.get('quantidadei')
            controlado = request.POST.get('controladoi')
            updateProduto = Produto(
                idproduto = idDoProduto,
                preco = preco,
                descricao = descricao,
                quantidade = quantidade,
                controlado = controlado
            )
            updateProduto.save()
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
        if nome and descricao and preco and quantidade and controlado:
            try:
                produtoNovo = Produto(
                    nome=nome,
                    descricao=descricao,
                    preco=preco,
                    quantidade=quantidade,
                    controlado=controlado
                )
                produtoNovo.save()
                messages.success(request, 'Produto adicionado com sucesso!')  
                return redirect('estoque')
            except:
                return messages.error(request, 'Erro ao adicionar')
        else:
            return messages.error(request, 'Preencha todos os dados necessario')
    return render(request, 'estoque/adicionar.html')