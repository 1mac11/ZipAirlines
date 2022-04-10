from rest_framework import serializers
from .models import Airplane
from .utils import get_airplane_per_minute_consumption, airplane_max_minutes_fly_capability


class AirplaneSerializer(serializers.ModelSerializer):
    per_minute = serializers.SerializerMethodField(source='get_per_minute')
    max_minutes = serializers.SerializerMethodField(source='get_max_minutes')

    class Meta:
        model = Airplane
        fields = ('airplane_id', 'passenger_assumptions', 'per_minute', 'max_minutes')

    @staticmethod
    def get_per_minute(obj) -> float:
        return get_airplane_per_minute_consumption(obj.airplane_id, obj.passenger_assumptions)

    @staticmethod
    def get_max_minutes(obj) -> float:
        return airplane_max_minutes_fly_capability(obj.airplane_id, obj.passenger_assumptions)
