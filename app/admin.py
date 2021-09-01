from django.contrib import admin
from .models import Foto, Projeto

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ['image', 'projeto']

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    list_filter = ['created_date']