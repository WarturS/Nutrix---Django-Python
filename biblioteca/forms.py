from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'fornecedor', 'ano_publicacao', 'quantidade', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'titulo': forms.TextInput(attrs={'placeholder': 'Título do livro'}),
            'autor': forms.TextInput(attrs={'placeholder': 'Nome do autor'}),
        }

    def clean_ano_publicacao(self):
        ano = self.cleaned_data.get('ano_publicacao')
        if ano and (ano < 1000 or ano > 9999):
            raise forms.ValidationError('Informe um ano válido (4 dígitos).')
        return ano
