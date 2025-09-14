from django.shortcuts import render, redirect
from .models import Livros
from .forms import LivroForm
import requests
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def listar_livros(request):
    livros = Livros.objects.all()
    if "q" in request.GET:
        termo = request.GET["q"]
        url = f"https://openlibrary.org/search.json?title={termo}"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            for item in dados["docs"][:5]:
                titulo = item.get("title")
                autor = ", ".join(item.get("author_name", [])) if item.get("author_name") else "Desconhecido"
                ano = item.get("first_publish_year")
                data_publicacao = None
                if ano:
                    data_publicacao = datetime(ano, 1, 1).date()
                livro_obj, created = Livros.objects.get_or_create(
                    titulo=titulo,
                    defaults={'autor': autor, 'data_publicacao': data_publicacao}
                )
                isbn_list = item.get("isbn", [])
                if isbn_list:
                    livro_obj.capa_url = f"https://covers.openlibrary.org/b/isbn/{isbn_list[0]}-M.jpg"
                else:
                    livro_obj.capa_url = None
                livro_obj.save()
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
    return render(request, 'criar_livro.html', {'form': form})

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
    return render(request, 'criar_livro.html', {'form': form})