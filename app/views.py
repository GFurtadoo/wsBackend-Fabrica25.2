from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor
from .forms import AutorForm
import requests
import re


def home_autores(request):
    return render(request, 'home_autores.html')


def listar_autores(request):
    if "q" in request.GET:
        termo = request.GET["q"]
        url = f"https://openlibrary.org/search/authors.json?q={termo}"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()

            for item in dados.get("docs", [])[:5]:
                nome = item.get("name") or "Desconhecido"
                key = item.get("key")  
                olid = key.split("/")[-1] if key else None

                bio = ""
                nacionalidade = ""

                if key:

                    detalhe_url = f"https://openlibrary.org{key}.json"
                    det_resp = requests.get(detalhe_url)
                    if det_resp.status_code == 200:
                        det = det_resp.json()


                        if isinstance(det.get("bio"), dict):
                            bio = det.get("bio", {}).get("value", "")
                        elif isinstance(det.get("bio"), str):
                            bio = det.get("bio")
                        else:
                            bio = ""


                        texto = (bio or "") + " " + " ".join(det.get("subjects", []))
                        m = re.search(
                            r'\b(Portuguese|Brazilian|French|English|Spanish|American|German|Italian)\b',
                            texto,
                            re.IGNORECASE
                        )
                        if m:
                            nacionalidade = m.group(1).capitalize()

           
                autor_obj, created = Autor.objects.get_or_create(
                    olid=olid,
                    defaults={
                        "nome": nome,
                        "biografia": bio,
                        "nacionalidade": nacionalidade,
                    }
                )

   
                updated = False
                if not autor_obj.biografia and bio:
                    autor_obj.biografia = bio
                    updated = True
                if not autor_obj.nacionalidade and nacionalidade:
                    autor_obj.nacionalidade = nacionalidade
                    updated = True
                if updated:
                    autor_obj.save()

    autores = Autor.objects.all()
    return render(request, 'listar_autores.html', {'autores': autores})


def criar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm()
    return render(request, 'criar_autor.html', {'form': form})

def atualizar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'criar_autor.html', {'form': form})


def deletar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    if request.method == 'POST':
        autor.delete()
        return redirect('listar_autores')
    return render(request, 'delete_autor.html', {'autor': autor})