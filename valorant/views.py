from rest_framework import generics
from .models import Arme, Agent, Map, Power
from .serializers import ArmeSerializer, AgentSerializer, MapSerializer, PowerSerializer


# ──────────────── Agents ────────────────

class AgentListAPIView(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


# ──────────────── Armes ────────────────

class ArmeListAPIView(generics.ListAPIView):
    queryset = Arme.objects.all()
    serializer_class = ArmeSerializer

class MapListAPIView(generics.ListAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

class PowerListAPIView(generics.ListAPIView):
    queryset = Power.objects.all()
    serializer_class = PowerSerializer 