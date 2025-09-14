from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'biografia', 'nacionalidade', 'foto_url']  # Adicione 'foto_url'
        widgets = {
            'biografia': forms.Textarea(attrs={'rows':4}),
        }