from django.shortcuts import render, redirect
from .models import Livros
from .forms import LivroForm
import requests

def home(request):
    return render(request, 'home.html')

def listar_livros(request):
    livros = Livros.objects.all()
    return render(request, 'list.html', {'livros': livros})

def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = LivroForm()
    return render(request, 'criar_livro.html', {'livros': form})


def deletar_livro(request, id):
    livro = Livros.objects.get(id=id)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar')
    return render(request, 'delete.html', {'livro': livro})

def atualizar_livro(request, pk):
    livro = Livros.objects.get(pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'criar_livro.html', {'livros': form})





