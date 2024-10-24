from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer


class MovieView(APIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request):
        movies = self.queryset.all()
        ser_data = self.serializer_class(movies, many=True)
        return Response(ser_data.data)

class MovieDetailView(APIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, pk):
        movie = self.queryset.get(pk=pk)
        ser_data = self.serializer_class(movie)
        return Response(ser_data.data)


class ReviewView(APIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request):
        reviews = self.queryset.all()
        ser_data = self.serializer_class(reviews, many=True)
        return Response(ser_data.data)
