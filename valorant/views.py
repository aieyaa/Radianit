from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_agents(request):
    agents = [
        {"id": 1, "name": "Jett", "role": "Duelist", "country": "South Korea"},
        {"id": 2, "name": "Phoenix", "role": "Duelist", "country": "United Kingdom"},
        {"id": 3, "name": "Sage", "role": "Sentinel", "country": "China"},
        {"id": 4, "name": "Sova", "role": "Initiator", "country": "Russia"},
    ]
    return Response(agents)
