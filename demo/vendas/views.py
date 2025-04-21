from django.shortcuts import render, get_object_or_404
from .models import Cliente, Pedido, Fornecedor, Produto, Pagamento

def home(request):
    return render(request,'vendas/index.html')

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

    fornecedores = Fornecedor.objects.all()

    if request.method == 'POST':
        idfornecedor = request.POST.get('idfornecedor')
        nome_produto = request.POST.get('nome_produto')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')

        try:
            fornecedor = Fornecedor.objects.get(id_fornecedor=idfornecedor)
            produtos = Produto(idfornecedor=fornecedor, nome_produto=nome_produto, preco=preco, estoque=estoque)
            produtos.save()
            sucesso = True
        except Fornecedor.DoesNotExist:
            # Fornecedor nao encontrado
            sucesso = False

        return render(request, 'vendas/criar_registro_do_produto.html', {
        'fornecedores': fornecedores,
        'sucesso': sucesso
        })

    return render(request, 'vendas/criar_registro_do_produto.html', {
        'fornecedores': fornecedores,
        'sucesso': sucesso
    })

def registrar_novo_pedido(request):
    sucesso = False

    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()

    if request.method == 'POST':
        id_cliente = request.POST.get('idcliente')
        nome_produto = request.POST.get('nome_produto')
        data_pedido = request.POST.get('data_pedido')
        total = request.POST.get('total')

        pedido = Pedido(idcliente=id_cliente, data_pedido=data_pedido, total=total)
        pedido.save()

        return render(request, 'vendas/registrar_novo_pedido.html', {
            'clientes': clientes, 
            'produtos': produtos,
            'sucesso': sucesso
        })
    
    return render(request, 'vendas/registrar_novo_pedido.html', 
        {'clientes': clientes, 
        'produtos': produtos,
        'sucesso': sucesso
    })

def verificar_pagamento(request):
    sucesso = False
    ids = Pedido.objects.values_list('id_pedido', flat=True)

    if request.method=='POST':
        id_pedido = request.POST.get('idpedido')
        metodo_de_pagamento = request.POST.get('metodo_pagamento')
        status_do_pagamento = request.POST.get('status_pagamento')
        valor = request.POST.get('valor')

        try:
            pedido = Pedido.objects.get(idcliente=id_pedido)
            pagamento = Pagamento(idpedido=id_pedido, metodo_pagamento=metodo_de_pagamento, status_pagamento=status_do_pagamento, valor=valor)
            pagamento.save()
            sucesso = True
        except Fornecedor.DoesNotExist:
            # Fornecedor nao encontrado
            sucesso = False

        return render(request, 'vendas/verificar_pagamento.html', {
            'sucesso': sucesso, 
            'ids': ids
        })

    return render(request, 'vendas/verificar_pagamento.html', {
            'sucesso': sucesso, 
            'ids': ids
    })
