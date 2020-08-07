from django.urls import path
from .views import Delivery, Catalogo, adicionaItem

urlpatterns = [
    path('delivery/',Delivery, name = 'delivery'),
    path('catalogo/',Catalogo, name = 'catalogo'),
    path('add-item/<int:id>',adicionaItem, name = 'adicionaItem')

]