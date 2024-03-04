import math

from django.core.paginator import Paginator


def fazer_escala_paginacao(
    escala_paginador,
    numero_paginas,
    pagina_atual,
):
    escala_intermediaria = math.ceil(numero_paginas / 2)
    escala_inicial = pagina_atual - escala_intermediaria
    escala_final = pagina_atual + escala_intermediaria
    total_paginas = len(escala_paginador)

    escala_inicial_offset = abs(escala_inicial) if escala_inicial < 0 else 0

    if escala_inicial < 0:
        escala_inicial = 0
        escala_final += escala_inicial_offset

    if escala_final >= total_paginas:
        escala_inicial = escala_inicial - abs(total_paginas - escala_final)

    paginacao = escala_paginador[escala_inicial:escala_final]
    return {
        'paginacao': paginacao,
        'escala_paginador': escala_paginador,
        'numero_paginas': numero_paginas,
        'pagina_atual': pagina_atual,
        'total_paginas': total_paginas,
        'escala_inicial': escala_inicial,
        'escala_final': escala_final,
        'primeira_pagina_fora_escala': pagina_atual > escala_intermediaria,
        'ultima_pagina_fora_escala': escala_final < total_paginas,
    }


def fazer_paginacao(request, queryset, qtd_por_pagina=12, numero_paginas=10):
    try:
        pagina_atual = int(request.GET.get('page', 1))
    except ValueError:
        pagina_atual = 1
    paginador = Paginator(queryset, qtd_por_pagina)
    pagina = paginador.get_page(pagina_atual)

    escala_paginacao = fazer_escala_paginacao(paginador.page_range, numero_paginas, pagina_atual)

    return pagina, escala_paginacao
