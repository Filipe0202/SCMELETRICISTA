from django import forms

from .models import Vendedor, Produto, Orcamento

class VendedorForm(forms.ModelForm):

    class Meta:
        model = Vendedor
        fields = ('nome', 'setor',)


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'descricao', 'valor', 'imagem', 'saldo')

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ('codigo_produto', 'valor_total', 'quantidade', 'codigo_vendedor',)


