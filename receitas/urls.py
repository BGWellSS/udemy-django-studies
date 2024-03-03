from django.urls import path

from receitas.apps import ReceitasConfig

from . import views

app_name = ReceitasConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    # https://docs.djangoproject.com/pt-br/5.0/topics/http/urls/
    path('receita/<int:id>/', views.receita, name='receita'),
]
