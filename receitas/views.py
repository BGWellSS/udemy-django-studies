from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'receitas/index.html', context={
        'nome_receita': 'Lasanha',
    }, status=200)


def receita(request, id):
    return render(request, 'receitas/pages/receita-view.html', context={
        'nome_receita': 'pizza',
    }, status=200)
