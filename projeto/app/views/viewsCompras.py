from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from ..models import Produto , SaidaMercadoria, Cliente
import datetime

### função de vendas
def index(request):
    if request.method == 'POST':
        idproduto = request.POST.get('id_produto')
        quantidade = request.POST.get('quantidade')
        valor = request.POST.get('valor')
        try:
            venda = SaidaMercadoria(
                quantidade = quantidade,
                valor = valor,
                datacompra = datetime.date.today,
                idproduto = idproduto
            )
            venda.save()
            # ele altera o banco de produto caso a venda seja feita
            produtoModel = get_object_or_404(Produto, idproduto=idproduto)
            quantidadeUpdrate = produtoModel.quantidade - quantidade
            produtoModel.quantidade = quantidadeUpdrate
            produtoModel.save()
            return messages.success(request, 'Cadastrada com sucesso')
        except:
            return messages.error(request, 'Erro ao salvar dados')
    produtos = Produto.objects.all()
    contexto = {'produtos': produtos}
    return render(request, 'compras/venda.html',contexto)

def menuVendas(request):
    return render(request, 'compras/menuVenda.html')

def estatisticasVendas(request):
    dataHoje = datetime.date.today()
    saida = SaidaMercadoria.objects.filter(datacompra=dataHoje).count()
    cliente = Cliente.objects.count()
    try:
        totalValor = SaidaMercadoria.objects.filter(datacompra=dataHoje).aaggregate(total=sum('valor'))['total'] or 0
    except (TypeError, ValueError):
        totalValor = 0
    contexto = {
        'saida': saida,
        'valor': totalValor,
        'cliente': cliente,
    }
    return render(request, 'compras/dashboard.html',  contexto)

def devolucao(request):
    if request.method == 'POST':
        idproduto = request.POST.get('id_produto')
        if idproduto:
            quantidade = request.POST.get('quantidade')
            motivo = request.POST.get('motivo')
            try:
                pass
            except:
                pass
    produtos = Produto.objects.all()
    contexto = {'produtos': produtos}
    return render(request, 'compras/devolucao.html', contexto)