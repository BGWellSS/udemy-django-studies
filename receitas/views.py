# from django.http import Http404
import os

from django.db.models import Q
from django.shortcuts import render

# from utils.receitas.gerador import fazer_receita
from utils.paginacao import fazer_paginacao

from .models import Receita

# Create your views here.

QTD_POR_PAGINA = int(os.environ.get('QTD_POR_PAGINA', 6))
NUMERO_PAGINACAO = int(os.environ.get('NUMERO_PAGINACAO', 10))


def index(request):
    receitas = Receita.objects.filter(publicada=True).order_by('-id')

    pagina, escala_paginacao = fazer_paginacao(request, receitas, QTD_POR_PAGINA, NUMERO_PAGINACAO)

    return render(request, 'receitas/pages/index.html', context={
        'receitas': pagina,
        'escala_paginacao': escala_paginacao,
    }, status=200)


def receita(request, id):
    receita = Receita.objects.filter(id=id, publicada=True).first()

    if not receita:
        return render(request, 'receitas/pages/404.html', context={
            'titulo': f'Receita - Não encontrada.',
        }, status=404)

    return render(request, 'receitas/pages/receita-view.html', context={
        'receita': receita,
        'titulo': f'{receita.titulo}',
        'tag_detalhe': True,
    }, status=200)


def categoria(request, categoria_id):
    # https://docs.djangoproject.com/pt-br/5.0/topics/db/queries/
    # Para filtrar dados usando uma Foreign Key (chave estrangeira), use o nome da chave seguido por dois
    #   sublinhados e o nome do campo da chave estrangeira.
    #     receitas = Receita.objects.filter(publicada=True, categoria__id=categoria_id).order_by('-id')

    # Forma de obter o nome da categoria
    #   categoria_nome = getattr(getattr(receitas.first(), 'categoria', None), 'nome', '404 - Sem Categoria')
    #
    # Alternativas para criar o erro 404
    """
        01-
        if not receitas:
            raise Http404('Categoria não encontrada.')

        categoria_nome = receitas.first().categoria.nome

        02-
        receitas = get_list_or_404(Receita.objects.filter(publicada=True, categoria__id=categoria_id).order_by('-id'))
        categoria_nome = receitas[0].categoria.nome
    """
    receitas = Receita.objects.filter(publicada=True, categoria__id=categoria_id).order_by('-id')

    pagina, escala_paginacao = fazer_paginacao(request, receitas, QTD_POR_PAGINA, NUMERO_PAGINACAO)

    if not pagina:
        return render(request, 'receitas/pages/404.html', context={
            'titulo': f'Categoria - Não encontrada.',
        }, status=404)

    categoria_nome = getattr(getattr(receitas.first(), 'categoria', None), 'nome', '404 - Sem Categoria')

    return render(request, 'receitas/pages/categoria.html', context={
        'receitas': pagina,
        'titulo': f'Categoria - {categoria_nome}',
        'escala_paginacao': escala_paginacao,
    }, status=200)


def busca(request):
    termo = request.GET.get('q', '').strip()

    if termo:
        receitas = Receita.objects.filter(
            Q(
                Q(titulo__icontains=termo) |
                Q(descricao__icontains=termo)
            ), publicada=True).order_by('-id')
    else:
        receitas = None

    pagina, escala_paginacao = fazer_paginacao(request, receitas, QTD_POR_PAGINA, NUMERO_PAGINACAO)

    return render(request, 'receitas/pages/busca.html', context={
        'receitas': pagina,
        'titulo': f'Busca - {termo}',
        'escala_paginacao': escala_paginacao,
        'termo': termo if termo else '🤔 Campo vazio ❌',
        'query_adicional': f'&q={termo}',
    }, status=200)
