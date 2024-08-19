# produtos/estoque/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('lista_estoque/', views.lista_estoque, name='lista_estoque'),
    path('criar_estoque/', views.criar_estoque, name='criar_estoque'),
    path('detalhe_estoque/<int:estoque_id>/', views.detalhe_estoque, name='detalhe_estoque'),
    path('atualizar_estoque/<int:estoque_id>/', views.atualizar_estoque, name='atualizar_estoque'),
    path('excluir_estoque/<int:estoque_id>/', views.excluir_estoque, name='excluir_estoque'),
]
