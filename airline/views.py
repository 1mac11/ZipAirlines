from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from airline.models import Airplane
from airline.serializers import AirplaneSerializer


class AirplaneViewSet(ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    @swagger_auto_schema(
        method='post',
        request_body=AirplaneSerializer(many=True),
        responses={201: openapi.Response('', AirplaneSerializer(many=True))}
    )
    @action(detail=False, methods=['post'], url_path='multi-create')
    def multi_create(self, request):
        serializer = self.serializer_class(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
