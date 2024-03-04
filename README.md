# Projeto de Estudos Django

Repositório de estudo do Curso "Aprenda Django Web Framework e Django Rest Framework com Python, HTML e CSS. Conheça o ORM, templates, Views, HTTP e +" da Udemy

## Tabela de Conteúdos

- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Util](#util)

## Instalação

### Clone o repositório

```ps
git clone https://github.com/BGWellSS/udemy-django-studies.git
cd udemy-django-studies
```

### Crie um ambiente virtual (recomendado)

- No Windows

```ps
py -m venv venv
```

- No Linux ou MacOS

```ps
python -m venv venv
```

### Ative o ambiente virtual

- No Windows:
  
```ps
.\venv\Scripts\activate
```

- No Unix ou MacOS:

```ps
source venv/bin/activate
```

### Instale as dependências

Com o ambiente virtual ativo:

```ps
pip install -r requirements.txt
```

## Configuração

Navegue até a pasta de configurações do projeto Django:

```ps
cd setup
```

Crie um arquivo .env na raiz do projeto e adicione as configurações de ambiente necessárias, como variáveis de configuração do banco de dados, chaves secretas, etc. (Este passo é opcional e depende de como você configurou seu projeto Django).

### Execute as migrações para criar a estrutura do banco de dados

Na raiz do projeto:

- No Windows

```ps
py .\manage.py migrate
```

- no Linux ou MacOS

```ps
python manage.py migrate
```

Caso necessario (alterações no models), prepare uma nova migração:

- No Windows

```ps
py .\manage.py makemigrations
```

- no Linux ou MacOS

```ps
python manage.py makemigrations
```

### Crie um superusuário para acessar o painel de administração

```ps
python manage.py createsuperuser
```

## Uso

Inicie o servidor de desenvolvimento:

- No Windows

```ps
py .\manage.py runserver
```

- no Linux ou MacOS

```ps
python manage.py runserver
```

### Endereço do aplicativo

<http://127.0.0.1:8000/>

### Painel de administração

<http://127.0.0.1:8000/admin>

## Util

Comandos uteis durante o desenvolvimento

### Duplicar receitas

```ps
py .\manage.py shell
```

```shell
from receitas.models import Receita
r = Receita.objects.get(pk=1)
for i in range(100): r.id = None; r.titulo = f'Foi duplicado {i}'; r.slug = f'foi-duplicado-{i}'; r.save();
```
