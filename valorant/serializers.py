from rest_framework import serializers
from .models import Capacite, Arme, Carte, Agent 

# Create your views here.

class CapaciteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacite
        fields = '__all__'

class ArmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arme
        fields = '__all__'

class CarteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carte
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    capacites = CapaciteSerializer(many=True, read_only=True)

    class Meta:
        model = Agent
        fields = '__all__'