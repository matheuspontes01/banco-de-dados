from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cliente, Pedido, Fornecedor, Produto

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
    if request.method == 'POST':
        nome_fornecedor = request.POST.get('nome_fornecedor')
        email = request.POST.get('email')
        telefone_fornecedor = request.POST.get('telefone_fornecedor')

        fornecedor = Fornecedor(nome_fornecedor=nome_fornecedor, email=email, telefone_fornecedor=telefone_fornecedor)
        fornecedor.save()

        return render(request, 'vendas/criar_novo_fornecedor.html', {'sucesso': True})

    return render(request, 'vendas/criar_novo_fornecedor.html')

def criar_registro_do_produto(request):
    sucesso = False

    ids = Fornecedor.objects.values_list('id_fornecedor', flat=True) 

    if request.method == 'POST':
        idfornecedor = request.POST.get('idfornecedor')
        nome_produto = request.POST.get('nome_produto')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')

        try:
            fornecedor = Fornecedor.objetcts.get(id_fornecedor=idfornecedor)
            produtos = Produto(idfornecedor=fornecedor, nome_produto=nome_produto, preco=preco, estoque=estoque)
            produtos.save()
            sucesso = True
        except Fornecedor.DoesNotExist:
            # Fornecedor nao encontrado
            sucesso = False

        return render(request, 'vendas/criar_registro_do_produto.html', {'sucesso': sucesso})

    return render(request, 'vendas/criar_registro_do_produto.html', {'ids': ids})

def registrar_novo_pedido(request):
    sucesso = False

    ids = Cliente.objects.values_list('id_cliente', flat=True) 

    if request.method == 'POST':
        id_cliente = request.POST.get('idcliente')
        data_pedido = request.POST.get('data_pedido')
        total = request.POST.get('total')

        try:
            cliente = Cliente.objects.get(id_cliente=id_cliente)
            pedido = Pedido(idcliente=cliente, data_pedido=data_pedido, total=total)
            pedido.save()
            sucesso = True
        except Cliente.DoesNotExist:
            # Cliente não encontrado
            sucesso = False

        return render(request, 'vendas/registrar_novo_pedido.html', {'sucesso': sucesso})
    
    return render(request, 'vendas/registrar_novo_pedido.html', {'ids': ids})

def verificar_pagamento(request):
    return render(request, 'vendas/verificar_pagamento.html')
