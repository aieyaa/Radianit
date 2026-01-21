from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from valorant.views import AgentViewSet, CapaciteViewSet, ArmeViewSet, CarteViewSet

outer = routers.DefaultRouter()
router.register('agents', AgentViewSet)
router.register('capacites', CapaciteViewSet)
router.register('armes', ArmeViewSet)
router.register('cartes', CarteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]