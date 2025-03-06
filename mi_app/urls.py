from django.urls import path
from .views import registrar_cliente, eliminar_cliente, editar_cliente, lista_clientes, inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('registrar/', registrar_cliente, name='registrar_cliente'),
    path('eliminar/<int:cliente_id>/', eliminar_cliente, name='eliminar_cliente'),
    path('editar/<int:cliente_id>/', editar_cliente, name='editar_cliente'),
]
