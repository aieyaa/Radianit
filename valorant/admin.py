from django.contrib import admin
from .models import Agent, Capacite, Arme, Carte

# Register your models here.
admin.site.register(Agent)
admin.site.register(Capacite)
admin.site.register(Arme)
admin.site.register(Carte)