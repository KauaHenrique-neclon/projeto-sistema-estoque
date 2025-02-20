from django.urls import path
from app.views import viewsEmpresa

urlpatterns = [
    path('MenuEmpresa/',viewsEmpresa.index,name='MenuEmpresa'),
    path('AdicionarCliente/',viewsEmpresa.adicionarClientes, name='AdicionarCliente'),
    path('desativarCliente/', viewsEmpresa.desativarClientes,name="desativarCliente"),
    path('adicionarFornecedor/',viewsEmpresa.adicionarFornecedor, name="adicionarFornecedor"),
    path('Entregas/', viewsEmpresa.EntregasFeitas,name='Entregas'),
    path('HistoricoEntregas/',viewsEmpresa.historiocoEntregas, name='HistoricoEntregas'),
]
