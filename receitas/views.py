from django.shortcuts import render

from utils.receitas.gerador import fazer_receita

from .models import Receita


# Create your views here.
def index(request):
    receitas = Receita.objects.filter(publicada=True).order_by('-id')

    return render(request, 'receitas/pages/index.html', context={
        'receitas': receitas,
    }, status=200)


def receita(request, id):
    return render(request, 'receitas/pages/receita-view.html', context={
        'receita': fazer_receita(),
        'tag_detalhe': True,
    }, status=200)


def categoria(request, categoria_id):
    # https://docs.djangoproject.com/pt-br/5.0/topics/db/queries/
    # Para filtrar dados usando uma Foreign Key (chave estrangeira), use o nome da chave seguido por dois
    #   sublinhados e o nome do campo da chave estrangeira.
    receitas = Receita.objects.filter(publicada=True, categoria__id=categoria_id).order_by('-id')

    return render(request, 'receitas/pages/categoria.html', context={
        'receitas': receitas,
        'categoria_nome': receitas[0].categoria.nome if receitas else '',
    }, status=200)
