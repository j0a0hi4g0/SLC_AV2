from django.contrib import admin
from .models import  Aplicacao, Lista, ListaCompras


admin.site.register(Lista)
admin.site.register(Aplicacao)
admin.site.register(ListaCompras)

