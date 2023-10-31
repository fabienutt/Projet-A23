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
        label="Description de l'inspection ",
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 50, 'class': 'custom-textarea'}),
        required=False)
    class Meta:
        model = Formulaire
        fields = ['content']
class TransportForm(forms.Form):
    type_vehicule = forms.ChoiceField(
        required=False,
        label="Milieu d'évolution",
        choices=[('Sélectionner','Sélectionner'),('Terrestre', 'Terrestre'), ('Aquatique', 'Aquatique'), ('Aérien', 'Aérien')],
        widget=forms.Select(attrs={'class': 'custom-select'})
    )
class ManipulationForm(forms.Form):
    content = forms.CharField(
        required=False,
        label='Description de la manipulation ',
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 50, 'class': 'custom-textarea'}))
    class Meta:
        model = Formulaire
        fields = ['content']

class TerrestreForm(forms.Form):
    type_vehicule = forms.ChoiceField(
        required=False,
        label="Type de déplacement",
        choices=[('Sélectionner','Sélectionner'),('Roues', 'Roues'), ('Chenilles', 'Chenilles')],
        widget=forms.Select(attrs={'class': 'custom-select'})
    )

class AquaForm(forms.Form):
    type_vehicule = forms.ChoiceField(
        required=False,
        label="Type de déplacement",
        choices=[('Sélectionner','Sélectionner'),('Moulin', 'Moulin'), ('Hélices', 'Hélices')],
        widget=forms.Select(attrs={'class': 'custom-select'})
    )

class AirForm(forms.Form):
    type_vehicule = forms.ChoiceField(
        label="Type de déplacement",
        choices=[('Sélectionner','Sélectionner'),('Hélices', 'Hélices'), ('Planeur', 'Planeur')],
        widget=forms.Select(attrs={'class': 'custom-select'})
    )

class ChoiceForm(forms.Form):
    intsaisie=forms.IntegerField(min_value=0,label="Nombre ")
    floatsaisie=forms.FloatField(min_value=0,label="Taille ")