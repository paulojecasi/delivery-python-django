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

def Delivery(request):


    produtosDoSite = Produto.objects.filter(site="SIM")
    bairroEntrega = Bairro.objects.filter(cobertura="S")
    tipo = "delivery"


    dados = {
        'ProdutosDoSite': produtosDoSite,
        'BairroEntrega': bairroEntrega,
        'Tipo': tipo

    }

    return render(request,'delivery.html',dados)

def Catalogo(request):


    produtosDoSite = Produto.objects.filter(site="SIM")
    bairroEntrega = Bairro.objects.filter(cobertura="S")
    tipo = "catalogo"

    dados = {
        'ProdutosDoSite': produtosDoSite,
        'BairroEntrega': bairroEntrega,
        'Tipo': tipo

    }

    return render(request,'catalogo.html',dados)