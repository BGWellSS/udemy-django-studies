import math


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
