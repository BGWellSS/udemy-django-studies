from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'receitas/index.html')


def contato(request):
    # return render(request, 'receitas/contato.html')
    return HttpResponse('CONTATO PAGE RECEITAS')


def sobre(request):
    # return render(request, 'receitas/sobre.html')
    return HttpResponse('SOBRE PAGE RECEITAS')
