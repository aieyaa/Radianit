from rest_framework import generics
from .models import Arme, Agent
from .serializers import ArmeSerializer, AgentSerializer


# ──────────────── Agents ────────────────

class AgentListAPIView(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


# ──────────────── Armes ────────────────

class ArmeListAPIView(generics.ListAPIView):
    queryset = Arme.objects.all()
    serializer_class = ArmeSerializer

