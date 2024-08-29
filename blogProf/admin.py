from django.contrib import admin
from .models import Eu

# Register your models here.

@admin.register(Eu)
class EuAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'email', 'senha', 'descricao')
    search_fields = ('nome', 'email')
    list_filter = ('idade', 'email')
    list_editable = ('email', 'senha')
    list_display_links = ('nome', 'descricao')
    list_max_show_all = 10