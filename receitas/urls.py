from django.urls import path

from . import views
from .apps import ReceitasConfig

app_name = ReceitasConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    # https://docs.djangoproject.com/pt-br/5.0/topics/http/urls/
    path('receita/busca/', views.busca, name='busca'),
    path('receita/categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('receita/<int:id>/', views.receita, name='receita'),
]
