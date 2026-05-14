from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cover = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Arme(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Map(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cover = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Power(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cover = models.ImageField(upload_to='images/', null=True, blank=True)
    agents = models.ManyToManyField('Agent', related_name='powers', blank=True)

    def __str__(self):
        return self.name
