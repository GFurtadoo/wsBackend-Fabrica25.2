from django.shortcuts import render, redirect
from .models import Livros
from .forms import LivroForm
import requests

def home(request):
    return render(request, 'home.html')



