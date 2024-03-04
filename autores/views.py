from django.shortcuts import render

from .forms import CadastroForm


# Create your views here.
def index(request):
    return render(request, 'autores/pages/index.html')


def cadastro(request):
    formulario = CadastroForm()

    return render(request, 'autores/pages/cadastro.html', context={
        'formulario': formulario
    }, status=200)
