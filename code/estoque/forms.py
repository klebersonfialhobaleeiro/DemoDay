from django import forms
from .models import Estoque

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['produto', 'quantidade']