# Generated by Django 5.1.4 on 2025-02-20 15:09

import datetime
import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idcliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, null=True)),
                ('telefone', models.IntegerField()),
                ('sobrenome', models.CharField(max_length=255, null=True)),
                ('cpf', models.CharField(max_length=11)),
                ('cnpj', models.CharField(max_length=18)),
                ('email', models.CharField(max_length=255, null=True)),
                ('bairro', models.CharField(max_length=255)),
                ('rua', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('cnpj', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('telefone', models.CharField(max_length=30)),
                ('nomeEmpresa', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255, null=True)),
                ('bairro', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('idproduto', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('preco', models.IntegerField()),
                ('descricao', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField()),
                ('controlado', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('idusuario', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_joined', models.DateField(default=datetime.date.today)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='RecebimentoMercadoria',
            fields=[
                ('idrecebeu', models.AutoField(primary_key=True, serialize=False)),
                ('datarecebeu', models.DateField(default=datetime.date.today)),
                ('totalproduto', models.IntegerField()),
                ('notaFiscal', models.IntegerField()),
                ('cnpj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.fornecedor')),
                ('idproduto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.produto')),
            ],
        ),
        migrations.CreateModel(
            name='SaidaMercadoria',
            fields=[
                ('idsaida', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('datacompra', models.DateField(default=datetime.date.today)),
                ('idproduto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.produto')),
            ],
        ),
    ]
