from django.db import models

class Autor(models.Model):
    nome = models.CharField('Nome', max_length=250)
    biografia = models.TextField('Biografia', blank=True, null=True)
    nacionalidade = models.CharField('Nacionalidade', max_length=100, blank=True, null=True)
    olid = models.CharField('OLID (OpenLibrary)', max_length=50, blank=True, null=True, unique=True)

    def __str__(self):
        return self.nome