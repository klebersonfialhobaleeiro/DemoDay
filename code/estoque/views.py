# produtos/estoque/views.py
from django.contrib.auth.decorators import login_required
from .models import Estoque
from .forms import EstoqueForm
from django.shortcuts import render, get_object_or_404, redirect

@login_required
def detalhe_estoque(request, estoque_id):
    estoque_item = get_object_or_404(Estoque, id=estoque_id)
    return render(request, 'estoque/detalhe_estoque.html', {'estoque_item': estoque_item})

@login_required
def lista_estoque(request):
    estoque_itens = Estoque.objects.all()
    return render(request, 'estoque/lista_estoque.html', {'estoque_itens': estoque_itens})

@login_required
def criar_estoque(request):
    if request.method == 'POST':
        form = EstoqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estoque')
    else:
        form = EstoqueForm()
    return render(request, 'estoque/criar_estoque.html', {'form': form})

@login_required
def atualizar_estoque(request, estoque_id):
    estoque_item = get_object_or_404(Estoque, id=estoque_id)
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_item)
        if form.is_valid():
            form.save()
            return redirect('lista_estoque')
    else:
        form = EstoqueForm(instance=estoque_item)
    return render(request, 'estoque/atualizar_estoque.html', {'form': form, 'estoque_item': estoque_item})

@login_required
def excluir_estoque(request, estoque_id):
    estoque_item = get_object_or_404(Estoque, id=estoque_id)
    if request.method == 'POST':
        estoque_item.delete()
        return redirect('lista_estoque')
    return render(request, 'estoque/excluir_estoque.html', {'estoque_item': estoque_item})
