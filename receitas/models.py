from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

# Create your models here.


class Receita(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.TextField(max_length=165)
    slug = models.SlugField()
    tempo_preparo = models.IntegerField()
    tempo_preparo_unidade = models.CharField(max_length=65)
    qtd_porcoes = models.IntegerField()
    qtd_porcoes_unidade = models.CharField(max_length=65)
    modo_preparo = models.TextField()
    modo_preparo_e_html = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    publicada = models.BooleanField(default=False)
    imagem_cover = models.ImageField(upload_to='receitas/covers/%Y/%m/%d/')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
