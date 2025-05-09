from django import forms

from demanda.cadastrodemanda.models import Demanda


class DemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = '__all__'

        widgets = {
            'descricao': forms.Textarea(attrs={
                'rows': 4,  # número de linhas visíveis
                'cols': 40,  # número de colunas visíveis
                'placeholder': 'Até 600 caracteres'
            }),
        }
