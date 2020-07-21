from django.urls import path
from .views import Produtos

urlpatterns = [
    path('delivery/',Produtos)

]