from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'vendas/index.html')

def cadastro_cliente(request):
    return render(request, 'vendas/cadastro_cliente.html')

def criar_novo_fornecedor(request):
    return render(request, 'vendas/criar_novo_fornecedor.html')

def criar_registro_do_produto(request):
    return render(request, 'vendas/criar_registro_do_produto.html')

def registrar_novo_pedido(request):
    return render(request, 'vendas/registrar_novo_pedido.html')

def verificar_pagamento(request):
    return render(request, 'vendas/verificar_pagamento.html')
