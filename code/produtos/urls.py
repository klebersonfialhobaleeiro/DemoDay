from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    # autenticação
    path("entrar/", LoginView.as_view(), name="entrar"),
    path("sair/", LogoutView.as_view(), name="sair"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("enviaremail/", views.enviarEmail, name="enviar-email"),

    # produtos
    path("produtos/lista_produtos/", views.lista_produtos, name="lista_produtos"),
    path('produtos/criar_produto/', views.criar_produto, name='criar_produto'),
    path('produtos/detalhes_produto/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('produtos/atualizar_produto/<int:produto_id>/', views.atualizar_produto, name='atualizar_produto'),
    path('produtos/excluir_produto/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),
]