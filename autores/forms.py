import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def add_atributo(campo, atributo, valor):
    atributo_atual = campo.widget.attrs.get(atributo, '')
    campo.widget.attrs[atributo] = f'{atributo_atual}{valor}'.strip()


def add_placeholder(campo, valor):
    add_atributo(campo, 'placeholder', valor)


def valida_senha_forte(senha):
    '''
    explicações:
        ^: Inicia a linha de correspondência.
        (?=.*[a-z]): A senha deve conter pelo menos uma letra minúscula.
        (?=.*[A-Z]): A senha deve conter pelo menos uma letra maiúscula.
        (?=.*\d): A senha deve conter pelo menos um dígito numérico.
        .{8,}: A senha deve ter pelo menos 8 caracteres de comprimento.
        $: Termina a linha de correspondência.
    '''

    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')

    if not regex.match(senha):
        raise ValidationError((
            'Senha inválida'
        ),
            code='invalid'
        )


class CadastroForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CadastroForm, self).__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Seu nome de usuário')
        add_placeholder(self.fields['email'], 'Seu e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: João')
        add_placeholder(self.fields['last_name'], 'Ex.: Silva')
        add_placeholder(self.fields['password'], '********')

    """
    # Exemplos de utilização de atributos
    # Sobrescrevendo os atributos de um campo

    first_name = forms.CharField(
        label='Nome',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'ex: João'}
        ),
    )
    """
    password = forms.CharField(
        label='Senha',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', }
        ),
        error_messages={
            'required': 'A senha não deve estar vazia'
        },
        help_text=(
            'Dica: A senha deve conter pelo menos,'
            ' uma letra maiúscula, uma minúscula,'
            ' um número, e ter 8 caracteres.'
        ),
        validators=[valida_senha_forte]
    )
    password_confirmacao = forms.CharField(
        label='Confirmação de senha',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'}
        ),
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        '''
        # Exemplos de utilização de atributos do Meta
        # Sobrescrevendo os atributos de um campo

        exclude = ['last_login', 'date_joined',
                    'is_superuser', 'is_staff', 'is_active',
                    'groups', 'user_permissions',]
        labels = {
            'username': 'Nome de usuário',
            'password': 'Senha',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
        }
        help_texts = {
            'username': 'Nome de usuário',
            'password': 'Senha',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
        }
        error_messages = {
            'username': {
                'max_length': "Nome de usuário muito longo.",
                'required': "Nome de usuário é obrigatório.",
                'min_length': "Nome de usuário muito curto.",
            },
        }
        widgets = {
            'username': forms.TextInput(attrs={
                            'class': 'form-control'
                            'placeholder': 'Nome de usuário'
                            }),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        '''

    def clean_password(self):
        data = self.cleaned_data.get('password')

        if 'atenção' in data:
            raise ValidationError(
                'Não digite %(pipoca)s no campo password',
                code='invalid',
                params={'pipoca': '"atenção"'}
            )

        return data

    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')

        if 'John Doe' in data:
            raise ValidationError(
                'Não digite %(value)s no campo first name',
                code='invalid',
                params={'value': '"John Doe"'}
            )

        return data

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirmacao = cleaned_data.get('password_confirmacao')

        if password != password_confirmacao:
            mensagem_erro_senhas_diferentes = ValidationError(
                'Os campos de senha não são iguais.',
                code='invalid'
            )
            raise ValidationError({
                'password': mensagem_erro_senhas_diferentes,
                'password_confirmacao': mensagem_erro_senhas_diferentes,
                # 'password_confirmacao': [mensagem_erro_senhas_diferentes, 'OUTRO_ERRO_AQUI'],
            })
