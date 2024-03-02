from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # return render(request, 'receitas/index.html')
    return HttpResponse('HOME PAGE RECEITAS')


def contato(request):
    # return render(request, 'receitas/index.html')
    return HttpResponse('CONTATO PAGE RECEITAS')


def sobre(request):
    # return render(request, 'receitas/index.html')
    return HttpResponse('SOBRE PAGE RECEITAS')
