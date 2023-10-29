from django.db import models
from django import forms

class Article(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Formulaire(models.Model):
    Texte = models.TextField()
    def __str__(self):
        return self.Texte


#---database--by--kl--(et--surtout--ChatGPT)-----------------------------
#Représente les composants individuels.
class component(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    fabricant = models.CharField(max_length=200, blank=True, null=True)
    # Vous pouvez ajouter d'autres champs pertinents ici.

    def __str__(self):
        return self.nom

#Représente les assemblages, qui sont des collections de composants.
class assembly(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    composants = models.ManyToManyField(component, through='complage')
    # Le champ `composants` est une relation many-to-many vers le modèle Composant.

    def __str__(self):
        return self.nom
    
#Table de jonction représente la relation entre un composant et un assemblage. 
#Elle peut également contenir des informations supplémentaires sur la relation, par exemple,
#la quantité de chaque composant dans un assemblage.
class complage(models.Model):
    composant = models.ForeignKey(component, on_delete=models.CASCADE)
    assemblage = models.ForeignKey(assembly, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    class Meta:
        unique_together = ['composant', 'assemblage']
        