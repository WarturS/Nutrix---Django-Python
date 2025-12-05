from django.contrib import admin
from .models import Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fornecedor', 'ano_publicacao', 'quantidade', 'criado_em')
    search_fields = ('titulo', 'autor', 'fornecedor')
    list_filter = ('ano_publicacao', 'fornecedor')
    ordering = ('-criado_em',)
