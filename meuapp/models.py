from django.db import models

class Livros(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    data_publicacao = models.DateField(null=True, blank=True)
    capa_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titulo