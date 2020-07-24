
from django.contrib import admin

# Register your models here.

from .models import(
    Cliente,
    Pedido,
    Entrega,
    Carrinho,
    Produto,
    Cidade,
    Bairro,
    Libera
)

class ProdutoAdmin(admin.ModelAdmin):
    #fields = ('cidade', 'estado')                  #-campos p/ aparecer no cadastro
    list_filter = ('bebida','site')               #-adc um filtro na tela
    search_fields = ('bebida','site')             #-cria um campo de busca

class CidadeAdmin(admin.ModelAdmin):
    #fields = ('cidade', 'estado')                  #-campos p/ aparecer no cadastro
    list_display = ('id','cidade','estado')         #-campos p/ aparecer na lista
    list_filter = ('estado','cidade')               #-adc um filtro na tela
    search_fields = ('cidade','estado')             #-cria um campo de busca

class BairroAdmin(admin.ModelAdmin):
    #fields = ('cidade', 'estado','bairro','zona','cobertura')                  #-campos p/ aparecer no cadastro
    list_display = ('id','cidade','bairro','zona','cobertura')         #-campos p/ aparecer na lista
    list_filter = ('cidade','bairro','zona','cobertura')               #-adc um filtro na tela
    search_fields = ('cidade','bairro','zona','cobertura')             #-cria um campo de busca

class LiberaAdmin(admin.ModelAdmin):
    #fields = ('cidade', 'estado')                  #-campos p/ aparecer no cadastro
    list_display = ('pagina','libera')  # -campos p/ aparecer na lista
    list_filter = ('pagina','libera')               #-adc um filtro na tela
    search_fields = ('pagina','libera')             #-cria um campo de busca


admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Entrega)
admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Carrinho)
admin.site.register(Cidade,CidadeAdmin)
admin.site.register(Bairro,BairroAdmin)
admin.site.register(Libera,LiberaAdmin)
