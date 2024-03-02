from django.urls import path

from receitas.views import contato, index, sobre

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),
]
