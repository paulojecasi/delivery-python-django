from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import (
    Cliente,
    Produto,
    Carrinho,
    Entrega,
    Pedido,
    Bairro,
    Libera
)

def Delivery(request):


    produtosDoSite = Produto.objects.filter(site="SIM")
    bairroEntrega = Bairro.objects.filter(cobertura="S")
    libera_delivery = Libera.objects.filter(pagina="delivery",libera="S")
    tipo = "delivery"


    dados = {
        'ProdutosDoSite': produtosDoSite,
        'BairroEntrega': bairroEntrega,
        'Tipo': tipo,
        'Libera_delivery':libera_delivery

    }

    if libera_delivery:
        return render(request,'delivery.html',dados)
    else:
        if request.user.is_authenticated:
            return render(request, 'delivery.html', dados)
        else:
            return render(request, 'siteNaoDisponivel.html', dados)


def Catalogo(request):


    produtosDoSite = Produto.objects.filter(site="SIM")
    bairroEntrega = Bairro.objects.filter(cobertura="S")
    tipo = "catalogo"
    libera_catalogo = Libera.objects.filter(pagina="catalogo",libera="S")

    dados = {
        'ProdutosDoSite': produtosDoSite,
        'BairroEntrega': bairroEntrega,
        'Tipo': tipo,
        'Libera_catalogo': libera_catalogo
    }

    if libera_catalogo:
        return render(request,'catalogo.html',dados)
    else:
        if request.user.is_authenticated:
            return render(request, 'catalogo.html', dados)
        else:
            return render(request, 'siteNaoDisponivel.html', dados)


def Administracao(request):

    ola = "OLA"

    dados = {
        'Ola': ola

    }

    return render(request, 'administracao.html', dados)

