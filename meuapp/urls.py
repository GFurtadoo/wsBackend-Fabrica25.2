from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listar/', views.listar_livros, name='listar'),
    path('create/', views.criar_livro, name='create'),
    path('delete/<int:id>/', views.deletar_livro, name='deletar_livro'),
    path('update/<int:pk>/', views.atualizar_livro, name='atualizar_livro'),
]