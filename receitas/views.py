# from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Receita

# from utils.receitas.gerador import fazer_receita


# Create your views here.
def index(request):
    receitas = Receita.objects.filter(publicada=True).order_by('-id')

    return render(request, 'receitas/pages/index.html', context={
        'receitas': receitas,
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

    if not receitas:
        return render(request, 'receitas/pages/404.html', context={
            'titulo': f'Categoria - Não encontrada.',
        }, status=404)

    categoria_nome = getattr(getattr(receitas.first(), 'categoria', None), 'nome', '404 - Sem Categoria')

    return render(request, 'receitas/pages/categoria.html', context={
        'receitas': receitas,
        'titulo': f'Categoria - {categoria_nome}',
    }, status=200)


def busca(request):
    termo = request.GET.get('q')

    if termo:
        receitas = Receita.objects.filter(publicada=True, titulo__icontains=termo).order_by('-id')
    else:
        receitas = None

    return render(request, 'receitas/pages/busca.html', context={
        'receitas': receitas,
        'titulo': f'Busca - {termo}',
        'termo': termo if termo else '🤔 Campo vazio ❌',
    }, status=200)
