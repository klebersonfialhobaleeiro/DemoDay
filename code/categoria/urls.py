from django.urls import path
from . import views

urlpatterns = [
    path('lista-categorias/', views.lista_categorias, name='lista_categorias'),
    path('detalhes-categoria/<int:categoria_id>/', views.detalhes_categoria, name='detalhes_categoria'),
    path('criar-categoria/', views.criar_categoria, name='criar_categoria'),
    path('atualizar-categoria/<int:categoria_id>/', views.atualizar_categoria, name='atualizar_categoria'),
    path('excluir-categoria/<int:categoria_id>/', views.excluir_categoria, name='excluir_categoria'),
]