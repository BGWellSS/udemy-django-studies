from django.urls import path

from receitas.views import index

urlpatterns = [
    path('', index, name='index'),
]
