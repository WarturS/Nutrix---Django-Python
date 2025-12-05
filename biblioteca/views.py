from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Livro
from .forms import LivroForm


def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, '<APP>/lista.html'.replace('<APP>', 'livros'), {'livros': livros})


def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm()
    return render(request, '<APP>/form.html'.replace('<APP>', 'livros'), {'form': form})


def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, '<APP>/form.html'.replace('<APP>', 'livros'), {'form': form, 'livro': livro})


def excluir_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')
    return render(request, '<APP>/confirmar_excluir.html'.replace('<APP>', 'livros'), {'livro': livro})