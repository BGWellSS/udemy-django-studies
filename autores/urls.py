from django.urls import path

from . import views
from .apps import AutoresConfig

app_name = AutoresConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro/validacao/', views.cadastro_validacao, name='validacao'),
]
