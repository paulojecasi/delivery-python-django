from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse
from .models import (
    Cliente,
    Produto,
    Carrinho,
    Entrega,
    Pedido,
    Bairro
)

def Produtos(request):


    produtosDoSite = Produto.objects.filter(site="SIM")
    bairroEntrega = Bairro.objects.filter(cobertura="S")

    dados = {
        'ProdutosDoSite': produtosDoSite,
        'BairroEntrega': bairroEntrega,

    }

    return render(request,'index.html',dados)