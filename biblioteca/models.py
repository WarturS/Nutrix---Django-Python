from django.db import models

class Livro(models.Model):
    titulo = models.CharField('Título', max_length=200)
    autor = models.CharField('Autor', max_length=150)
    fornecedor = models.CharField('Fornecedor', max_length=150)
    ano_publicacao = models.PositiveIntegerField('Ano de publicação')
    quantidade = models.PositiveIntegerField('Quantidade disponível', default=0)
    descricao = models.TextField('Descrição', blank=True, null=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.titulo} — {self.autor}"
