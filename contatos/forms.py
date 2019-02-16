from django.forms import ModelForm, TextInput
from .models import Empresa

class EmpresaForm(ModelForm):
   class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control'}),
            'cnpj': TextInput(attrs={'class':'form-control'}),
            'endereco': TextInput(attrs={'class':'form-control'}),
            'contato': TextInput(attrs={'class':'form-control'}),
            'descricao': TextInput(attrs={'class':'form-control'}),
        }

