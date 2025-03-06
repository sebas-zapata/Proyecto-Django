from django.urls import path
from .views import registrar_cliente, lista_clientes, inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('registrar/', registrar_cliente, name='registrar_cliente'),
]
