from django import forms
from django.db import models
from .models import Formulaire

class FormulaireForm(forms.ModelForm):
    content = forms.CharField(
        required=False,
        label='Description de votre robot ',
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}))
    class Meta:
        model = Formulaire
        fields = ['content']



class InspectionForm(forms.Form):
    content = forms.CharField(
        label="Description de l'inspection ",
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 50, 'class': 'custom-textarea'}),
        required=False)
    
class TransportForm(forms.Form):
    type_vehicule = forms.ChoiceField(
        required=False,
        label="Milieu d'évolution",
        choices=[('Sélectionner','Sélectionner'),('Terrestre', 'Terrestre'), ('Aquatique', 'Aquatique'), ('Aérien', 'Aérien')],
        widget=forms.Select(attrs={'class': 'custom-select'})
    )
class ManipulationForm(forms.Form):
    content2 = forms.CharField(
        required=False,
        label='Description de la manipulation ',
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 50, 'class': 'custom-textarea'}))
    

class TerrestreForm(forms.Form):
    
    choices=[('Wheels', 'Wheels'), ('Crawlers', 'Crawlers')]
    
    votre_champ_radio = forms.ChoiceField(
        choices=choices,
        widget=forms.RadioSelect
    )

class AquaForm(forms.Form):
    
    choices=[('Water mill', 'Water mill'), ('airblades (water)', 'Airblades (water)')]
    
    votre_champ_radio = forms.ChoiceField(
        choices=choices,
        widget=forms.RadioSelect
    )

class AirForm(forms.Form):
    
    choices=[('Airblades (air)', 'Airblades (air)'), ('Glider', 'Glider')]
        
    votre_champ_radio = forms.ChoiceField(
        choices=choices,
        widget=forms.RadioSelect
    )

class ChoiceForm(forms.Form):
    intsaisie=forms.IntegerField(min_value=0,label="Nombre ")
    floatsaisie=forms.FloatField(min_value=0,label="Taille (cm) ")