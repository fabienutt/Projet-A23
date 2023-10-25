from django import forms
from django.db import models
from .models import Formulaire

class FormulaireForm(forms.ModelForm):
    content = forms.CharField(
        label='Description de votre robot ',
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}))
    class Meta:
        model = Formulaire
        fields = ['content']

from django import forms

class InspectionForm(forms.Form):
    content = forms.CharField(
        label="Description de l'inspection : ",
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}))
    class Meta:
        model = Formulaire
        fields = ['content']
class TransportForm(forms.Form):
    type_vehicule = forms.ChoiceField(label="Milieu d'évolution",choices=[('Terrestre', 'Terrestre'), ('Aquatique', 'Aquatique'),('Aérien', 'Aérien ')])
    
class ManipulationForm(forms.Form):
    content = forms.CharField(
        label='Description de la manipulation : ',
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}))
    class Meta:
        model = Formulaire
        fields = ['content']