from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("<int:aplicacao_id>", views.aplicacao, name="aplicacao"),
    path('cadastro', views.cadastro, name='cadastro'),
    path('logar', views.logar, name='logar'),
    path('pagina', views.pagina, name='pagina'),
    path('inicio', views.inicio, name='inicio')
]