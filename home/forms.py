from django import forms
from .models import Formulaire


class FormulaireForm(forms.Form):
    Texte = forms.CharField(label='Nom de l\'équipe A',max_length=100)
    