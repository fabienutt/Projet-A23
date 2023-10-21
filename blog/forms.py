from django import forms
from .models import Formulaire

class FormulaireForm(forms.ModelForm):
    content = forms.CharField(
        label='Description de votre robot ',
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}))
    class Meta:
        model = Formulaire
        fields = ['content']
