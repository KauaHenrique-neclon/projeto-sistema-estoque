from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Cliente, Produto, Fornecedor, RecebimentoMercadoria, SaidaMercadoria

def dashboard(request):
    totalClinte = Cliente.objects.count()
    totalProdutos = Produto.objects.count()
    totalFornecedor = Fornecedor.objects.count()
    ultimasTresVendas = SaidaMercadoria.objects.order_by('-datacompra')[:3]
    dados = {
        'totalCliente': totalClinte,
        'totalProdutos': totalProdutos,
        'totalFornecedor': totalFornecedor,
        'ultimasTresVendas': ultimasTresVendas,
    }
    return render(request, 'dashboard/dashboard.html',dados)




# só estou deixando alguns pensamentos
"""
    eu fiz esse sistema em 2 semanas sozinho contruido tudo
    estou cansado de ir pro trabalho no shopping e ver uma mina lá
    eu fiz de tudo pela pessoa mas me fazde otario, eu corri atras
    mas ela me jogou pra friendzone e falei 'tudo bem', mas eu queria
    sair fora e esquece ela, queria nunca mais falar com ela, mas ela 
    sempre me chama pra conversar, eu vou que nem cachorrinho de falar
    com ela, estou cansado, a unica coisa que me aceita é a programação,
    eu estou todo cansado e morto, passei mt noites virado pensando nela
    e pensando no futuro, eu já não tenho mais paz, depois da Gleicy
    eu disse que ia ficar quieto e em paz, sem aceita absolumente nada
    mas eu estou voltando a ter sentimentos sobre pessoas, mas tudo bem
    a vida é feita de escolha, e eu escolho seguir 
"""