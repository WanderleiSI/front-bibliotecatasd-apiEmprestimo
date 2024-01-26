from django import forms
from .models import Emprestimo

class FormEmprestimo(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['titulo', 'idCliente', 'idLivro', 'dataDevolucao']
