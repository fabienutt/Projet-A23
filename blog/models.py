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