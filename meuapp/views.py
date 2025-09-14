from django.shortcuts import render, redirect
from .models import Livro, Autor, Categoria
from .forms import LivroForm
import requests
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def listar_livros(request):
    livros = Livro.objects.all()
    if "q" in request.GET:
        termo = request.GET["q"]
        url = f"https://openlibrary.org/search.json?title={termo}"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            categoria_padrao, _ = Categoria.objects.get_or_create(nome="Sem categoria")
            for item in dados["docs"][:5]:
                titulo = item.get("title")
                autor_nome = ", ".join(item.get("author_name", [])) if item.get("author_name") else "Desconhecido"
                ano = item.get("first_publish_year")
                data_publicacao = None
                if ano:
                    data_publicacao = datetime(ano, 1, 1).date()
                autor_obj, _ = Autor.objects.get_or_create(nome=autor_nome)
                livro_obj, created = Livro.objects.get_or_create(
                    titulo=titulo,
                    autor=autor_obj,
                    categoria=categoria_padrao,
                    defaults={'data_publicacao': data_publicacao}
                )
                isbn_list = item.get("isbn", [])
                if isbn_list:
                    livro_obj.capa_url = f"https://covers.openlibrary.org/b/isbn/{isbn_list[0]}-M.jpg"
                else:
                    livro_obj.capa_url = None
                livro_obj.save()
    livros = Livro.objects.all()
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
    livro = Livro.objects.get(id=id)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar')
    return render(request, 'delete.html', {'livro': livro})

def atualizar_livro(request, pk):
    livro = Livro.objects.get(pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'criar_livro.html', {'form': form})