from django.shortcuts import render

from utils.receitas.gerador import fazer_receita


# Create your views here.
def index(request):
    return render(request, 'receitas/pages/index.html', context={
        'receitas': [fazer_receita() for _ in range(10)],
    }, status=200)


def receita(request, id):
    return render(request, 'receitas/pages/receita-view.html', context={
        'receita': fazer_receita(),
        'tag_detalhe': True,
    }, status=200)
