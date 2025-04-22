from django.contrib import admin
from django.urls import path, include
from vendas import views
from vendas.views import home


urlpatterns = [
    path('',home),
    path('cadastro-cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('novo-fornecedor/', views.criar_novo_fornecedor, name='criar_novo_fornecedor'),
    path('novo-produto/', views.criar_registro_do_produto, name='criar_registro_do_produto'),
    path('novo-pedido/', views.registrar_novo_pedido, name='registrar_novo_pedido'),
    path('verificar-pagamento/', views.verificar_pagamento, name='verificar_pagamento'),
    
]

