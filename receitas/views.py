from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'receitas/index.html', context={
        'nome_receita': 'Lasanha',
    }, status=200)
