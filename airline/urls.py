from django.urls import path, include
from rest_framework import routers

from airline.views import AirplaneViewSet

router = routers.DefaultRouter()
router.register(r'airplanes', AirplaneViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
