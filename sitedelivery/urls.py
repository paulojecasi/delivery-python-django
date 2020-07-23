from django.urls import path
from .views import Delivery, Catalogo, Administracao

urlpatterns = [
    path('delivery/',Delivery),
    path('catalogo/',Catalogo),
    path('controle/',Administracao)

]