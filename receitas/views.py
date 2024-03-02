from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'receitas/index.html', context={
        'nome_receita': 'Lasanha',
    }, status=200)


def contato(request):
    return render(request, 'receitas/contato.html')


def sobre(request):
    # return render(request, 'receitas/sobre.html')
    return HttpResponse('SOBRE PAGE RECEITAS')
