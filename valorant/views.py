from django.shortcuts import render
from rest_framework import viewsets
from .models import Agent, Capacite, Arme, Carte
from .serializers import (
    AgentSerializer, CapaciteSerializer, ArmeSerializer,
    CarteSerializer,
)

# Create your views here.

class AgentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class CapaciteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Capacite.objects.all()
    serializer_class = CapaciteSerializer


class ArmeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Arme.objects.all()
    serializer_class = ArmeSerializer

class CarteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Carte.objects.all()
    serializer_class = CarteSerializer

