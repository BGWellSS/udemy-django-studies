from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CadastroForm


# Create your views here.
def index(request):
    return render(request, 'autores/pages/index.html', context={
        'titulo': 'Autores - Home',
    }, status=200)


def cadastro(request):

    dados_formulario_cadastro = request.session.get('dados_formulario_cadastro', None)

    formulario = CadastroForm(dados_formulario_cadastro)

    return render(request, 'autores/pages/cadastro.html', context={
        'titulo': 'Autores - Cadastro',
        'formulario': formulario,
        'acao_formulario': reverse('autores:validacao'),
    }, status=200)


def cadastro_validacao(request):

    if not request.POST:
        return redirect('autores:index')

    POST = request.POST
    request.session['dados_formulario_cadastro'] = POST
    formulario = CadastroForm(POST)

    if formulario.is_valid():
        usuario = formulario.save(commit=False)
        usuario.set_password(usuario.password)
        usuario.save()
        messages.success(request, 'Usuario cadastrado com sucesso!')
        del request.session['dados_formulario_cadastro']

    return redirect('autores:cadastro')
