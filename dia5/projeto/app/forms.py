from django import forms
from .models import EnderecoCep

class EnderecoCepForm(forms.ModelForm):
    class Meta:
        model = EnderecoCep
        fields = ['cep']
        labels = {
            'cep': 'CEP'
        }
        widgets = {
            'cep': forms.TextInput(attrs={'placeholder': 'Digite um CEP'})
        }