from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Produto 
from .forms import ProdutoForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from django.contrib import messages
from django.core import mail
from django.conf import settings

def cadastro(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'registration/registration.html', context)

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
    return redirect('entrar')

def enviarEmail(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        if nome and email and mensagem:
                try:
                    from_email = settings.EMAIL_HOST_USER
                    connection = mail.get_connection()
                    connection.open()
                    email_empresa = mail.EmailMessage(f'Novo contato de {nome}', f'{nome} com o email: {email}\n tem a seguinte dúvida: {mensagem}', from_email,
                    ["contato@agapecuidadores.com"], connection=connection)
                    email_cliente = mail.EmailMessage(f'Obrigado {nome}', f'Obrigado {nome} por entrar em contato conosco! Nós vamos responder para você o mais rápido possível.', from_email,
                    [email], connection=connection)
                    
                    connection.send_messages([email_empresa, email_cliente])
                    connection.close()

                    messages.add_message(request, messages.SUCCESS, 'Mensagem enviada')
                except Exception as e:
                    messages.add_message(request, messages.ERROR, 'Erro ao enviar a menssagem')
        else:
            messages.add_message(request, messages.ERROR, 'Preencha os campos')
        return redirect(f"{reverse('home')}#contato")

@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

@login_required
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save()
            return redirect('detalhes_produto', produto_id=produto.id)
    else:
        form = ProdutoForm()
    return render(request, 'produtos/criar_produto.html', {'form': form})

@login_required
def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'produtos/detalhes_produto.html', {'produto': produto})

@login_required
def atualizar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('detalhes_produto', produto_id=produto.id)
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/atualizar_produto.html', {'form': form, 'produto': produto})

@login_required
def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos/excluir_produto.html', {'produto': produto})