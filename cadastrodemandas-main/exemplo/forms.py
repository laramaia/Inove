from django import forms

from exemplo.models import Solucao


class SolucaoForm(forms.ModelForm):
    class Meta:
        model = Solucao
        fields = '__all__'
        

        widgets = {
            'descricao': forms.Textarea(attrs={
                'rows': 4,  # número de linhas visíveis
                'cols': 40,  # número de colunas visíveis
                'placeholder': 'Até 600 caracteres'
            }),
        }