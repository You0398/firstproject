from django.db import models
from datetime import datetime

# Create your models here.

class Article(models.Model):
    nom = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class Entree(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now)

class Sortie(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now)