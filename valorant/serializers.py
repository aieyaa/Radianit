from rest_framework import serializers
from .models import Agent, Arme, Map, Power

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class ArmeSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = Arme
        fields = '__all__'

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'

class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        fields = '__all__'
