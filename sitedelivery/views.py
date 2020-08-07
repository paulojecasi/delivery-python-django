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


def adicionaItem(request,id):

    if request.method == 'POST':
        itemDopedido = Produto.objects.get(id=id)


        carrinhoAdd = Carrinho();

        carrinhoAdd.produto = itemDopedido;
        carrinhoAdd.valor_unitario = request.POST.get('valor_unitario');
        carrinhoAdd.quantidade = request.POST.get('quantidade');
        carrinhoAdd.valor_total_item = request.POST.get('valor_total_item');
        carrinhoAdd.situacao_carrinho = 0;

        carrinhoAdd.save()

        messages.success(request, 'Item foi adicionado no carrinho')
        return redirect('delivery')





