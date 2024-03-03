from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # https://docs.djangoproject.com/pt-br/3.2/topics/http/urls/
    path('receita/<int:id>/', views.receita, name='receita'),
]
