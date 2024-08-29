from django.contrib import admin
from .models import Guilherme, Curso

# Register your models here.

@admin.register(Guilherme)
class GuilhermeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'email', 'senha', 'descricao')
    search_fields = ('nome', 'email')
    list_filter = ('idade', 'email')
    list_editable = ('email', 'senha')
    list_display_links = ('nome', 'descricao')
    list_max_show_all = 10

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem')
    search_fields = ('nome',)
    list_filter = ('nome',)
    list_editable = ('imagem',)
    list_display_links = ('nome',)
    list_max_show_all = 10