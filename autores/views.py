from django.shortcuts import render

from .forms import CadastroForm


# Create your views here.
def index(request):
    return render(request, 'autores/pages/index.html', context={
        'titulo': 'Autores - Home',
    }, status=200)


def cadastro(request):

    if request.POST:
        formulario = CadastroForm(request.POST)
    else:
        formulario = CadastroForm()

    return render(request, 'autores/pages/cadastro.html', context={
        'titulo': 'Autores - Cadastro',
        'formulario': formulario
    }, status=200)
