from django.contrib import admin
from .models import  Aplicacao, Lista



class AplicacaoInline(admin.StackedInline):
    model = Aplicacao

class ListaAdmin(admin.ModelAdmin):
    inlines = [AplicacaoInline]
    list_display = ['nome', 'total']

admin.site.register(Lista, ListaAdmin)
admin.site.register(Aplicacao)


