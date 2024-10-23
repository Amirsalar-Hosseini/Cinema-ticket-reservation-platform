from rest_framework.response import Response
from .models import Cinema, Screen, Location
from .serializers import CinemaSerializer, ScreenSerializer, LocationSerializer
from rest_framework.views import APIView


class CinemaView(APIView):
    queryset = Cinema.objects
    serializer_class = CinemaSerializer

    def get(self, request):
        cinemas = self.queryset.all()
        serializer = self.serializer_class(cinemas, many=True)
        return Response(serializer.data)


class ScreenView(APIView):
    queryset = Screen.objects
    serializer_class = ScreenSerializer

    def get(self, request):
        screens = self.queryset.all()
        serializer = self.serializer_class(screens, many=True)
        return Response(serializer.data)

class LocationView(APIView):
    queryset = Location.objects
    serializer_class = LocationSerializer

    def get(self, request):
        locations = self.queryset.all()
        serializer = self.serializer_class(locations, many=True)
        return Response(serializer.data)

