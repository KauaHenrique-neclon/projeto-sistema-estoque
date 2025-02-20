from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
import datetime

# Create your models here.

class Produto(models.Model):
    idproduto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False)
    preco = models.IntegerField(null=False)
    descricao = models.CharField(max_length=255,null=False)
    quantidade = models.IntegerField(null=False)
    controlado = models.CharField(max_length=30, null=False)
    is_active = models.BooleanField(default=True)

class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=16,null=False,primary_key=True)
    telefone = models.CharField(max_length=30, null=False)
    nomeEmpresa = models.CharField(max_length=255, null=False)
    endereco = models.CharField(max_length=255, null=True)
    bairro = models.CharField(max_length=255, null=False)
    numero = models.IntegerField(null=False)

class SaidaMercadoria(models.Model):
    idsaida = models.AutoField(primary_key=True)
    quantidade = models.IntegerField(null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    datacompra = models.DateField(default=datetime.date.today)
    idproduto = models.ForeignKey(Produto,to_field='idproduto',on_delete=models.CASCADE,null=True)

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=True)
    telefone = models.IntegerField( null=False)
    sobrenome = models.CharField(max_length=255, null=True)
    cpf = models.CharField(max_length=11)
    cnpj = models.CharField(max_length=18)
    email = models.CharField(max_length=255, null=True)
    bairro = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    numero = models.IntegerField()
    is_active = models.BooleanField(default=True)

class RecebimentoMercadoria(models.Model):
    idrecebeu = models.AutoField(primary_key=True)
    datarecebeu = models.DateField(default=datetime.date.today)
    totalproduto = models.IntegerField()
    notaFiscal = models.IntegerField()
    cnpj = models.ForeignKey(Fornecedor,to_field='cnpj',on_delete=models.CASCADE,null=True)
    idproduto = models.ForeignKey(Produto,to_field='idproduto',on_delete=models.CASCADE,null=True)

class Usuario(AbstractUser):
    idusuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    date_joined = models.DateField(default=datetime.date.today)
    email = models.EmailField(blank=True,unique=True ,null=True)