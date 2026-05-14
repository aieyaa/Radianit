import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from valorant.models import Agent

def seed_agents():
    agents_data = [
        {"name": "Jett", "role": "Duelist", "country": "South Korea", "description": "Representing her home country of South Korea, Jett's agile and evasive fighting style lets her take risks no one else can."},
        {"name": "Phoenix", "role": "Duelist", "country": "United Kingdom", "description": "Hailing from the U.K., Phoenix's star power shines through in his fighting style, igniting the battlefield with flash and flare."},
        {"name": "Sage", "role": "Sentinel", "country": "China", "description": "The stronghold of China, Sage creates safety for herself and her team wherever she goes."},
        {"name": "Sova", "role": "Initiator", "country": "Russia", "description": "Born from the eternal winter of Russia's tundra, Sova tracks, finds, and eliminates enemies with ruthless efficiency and precision."},
        {"name": "Brimstone", "role": "Controller", "country": "USA", "description": "Joining from the USA, Brimstone's orbital arsenal ensures his team always has the advantage."},
    ]

    for data in agents_data:
        Agent.objects.get_or_create(
            name=data["name"],
            defaults={
                "role": data["role"],
                "country": data["country"],
                "description": data["description"]
            }
        )
    print("Base de donnees peuplee avec succes !")

if __name__ == "__main__":
    seed_agents()
