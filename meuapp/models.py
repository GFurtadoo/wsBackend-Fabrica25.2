from django.db import models

class Livros(models.Model):
        titulo = models.CharField(max_length=100)
        autor = models.CharField(max_length=100)
        data_publicacao = models.DateField()
