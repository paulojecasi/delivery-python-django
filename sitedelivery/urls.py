from django.urls import path
from .views import Delivery, Catalogo

urlpatterns = [
    path('delivery/',Delivery),
    path('catalogo/',Catalogo)

]