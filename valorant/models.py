from django.db import models

# Create your models here.

class Agent(models.Model):
    nom          = models.CharField(max_length=50, unique=True)
    role         = models.CharField(max_length=20, choices=[('Duelist','Duelist'), ('Controller','Controller'), ('Sentinel','Sentinel'),('Initiator','Initiator')])
    pays         = models.CharField(max_length=50, blank=True)   
    date_sortie  = models.DateField()              
    biographie   = models.TextField(blank=True)
    img = models.ImageField(upload_to='images/%Y/%m', blank=True)

class Capacite(models.Model):
    agent       = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="capacites")
    nom         = models.CharField(max_length=100)
    cout        = models.IntegerField(null=True, blank=True)
    description = models.TextField()

class Arme(models.Model):
    nom         = models.CharField(max_length=50, unique=True)
    categorie   = models.CharField(max_length=20)
    prix        = models.PositiveIntegerField()
    degats      = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/%Y/%m', blank=True)        

class Carte(models.Model):
    nom             = models.CharField(max_length=50, unique=True)   
    description     = models.TextField(blank=True)
    localisation    = models.CharField(max_length=100, blank=True)
    img = models.ImageField(upload_to='images/%Y/%m', blank=True)
