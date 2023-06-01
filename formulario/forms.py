from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['tipo_pessoa', 'nome', 'cpf', 'razao_social', 'cnpj']
