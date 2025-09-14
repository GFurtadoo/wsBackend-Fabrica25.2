from django.urls import path
from . import views

urlpatterns = [
    path('autores/home/', views.home_autores, name='home_autores'),
    path('autores/', views.listar_autores, name='listar_autores'),
    path('autores/create/', views.criar_autor, name='criar_autor'),
    path('autores/update/<int:pk>/', views.atualizar_autor, name='atualizar_autor'),
    path('autores/delete/<int:pk>/', views.deletar_autor, name='deletar_autor')
]