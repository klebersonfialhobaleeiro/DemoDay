from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Categoria
from .forms import CategoriaForm

@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista_categorias.html', {'categorias': categorias})

@login_required
def detalhes_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    return render(request, 'categorias/detalhes_categoria.html', {'categoria': categoria})

@login_required
def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            return redirect('detalhes_categoria', categoria_id=categoria.id)
    else:
        form = CategoriaForm()
    return render(request, 'categorias/criar_categoria.html', {'form': form})

@login_required
def atualizar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('detalhes_categoria', categoria_id=categoria.id)
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/atualizar_categoria.html', {'form': form, 'categoria': categoria})

@login_required
def excluir_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'categorias/excluir_categoria.html', {'categoria': categoria})
