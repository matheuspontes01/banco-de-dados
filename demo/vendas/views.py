from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente

def index(request):
    return render(request, 'vendas/index.html')

def cadastro_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')

        cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone)
        cliente.save()

        return render(request, 'vendas/cadastro_cliente.html', {'sucesso': True})

    return render(request, 'vendas/cadastro_cliente.html')

def criar_novo_fornecedor(request):
    return render(request, 'vendas/criar_novo_fornecedor.html')

def criar_registro_do_produto(request):
    return render(request, 'vendas/criar_registro_do_produto.html')

def registrar_novo_pedido(request):
    return render(request, 'vendas/registrar_novo_pedido.html')

def verificar_pagamento(request):
    return render(request, 'vendas/verificar_pagamento.html')
