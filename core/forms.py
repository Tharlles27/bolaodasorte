from django import forms
from .models import Pessoa, Escolha
from .models import Rodadas, Dezenas, Config

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('nome', 'telefone', 'repeticao', 'pagamento') 



class EscolhaForm(forms.ModelForm):
    class Meta:
        model = Escolha
        fields = ('__all__')


class RodadasForm(forms.ModelForm):
    class Meta:
        model = Rodadas
        fields = ('__all__') 

class DezenasForm(forms.ModelForm):
    class Meta:
        model = Dezenas
        fields = ('__all__')


class ConfigForm(forms.ModelForm):
    class Meta:
        model = Config
        fields = ('__all__')