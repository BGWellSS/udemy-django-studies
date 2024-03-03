# from inspect import signature
from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def fazer_receita():
    return {
        'id': fake.random_number(digits=6, fix_len=True),
        'titulo': fake.sentence(nb_words=6),
        'descricao': fake.sentence(nb_words=12),
        'tempo_preparo': fake.random_number(digits=2, fix_len=True),
        'tempo_preparo_unidade': 'Minutos',
        'qtd_porcoes': fake.random_number(digits=2, fix_len=True),
        'qtd_porcoes_unidade': 'Porção',
        'modo_preparo': fake.text(3000),
        'criado_em': fake.date_time(),
        'autor': {
            'nome_primeiro': fake.first_name(),
            'nome_final': fake.last_name(),
        },
        'categoria': {
            'nome': fake.word()
        },
        'imagem_cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(fazer_receita())
