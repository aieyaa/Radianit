from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('agents/', views.AgentListAPIView.as_view()),
    path('armes/', views.ArmeListAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)