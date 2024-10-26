from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework.pagination import PageNumberPagination


class MovieView(APIView):
    pagination_class = PageNumberPagination
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request):
        movies = self.queryset.all()
        paginator = self.pagination_class()
        paginator.page_size = 10
        paginated_movies = paginator.paginate_queryset(movies, request)
        ser_data = self.serializer_class(paginated_movies, many=True)
        return paginator.get_paginated_response(ser_data.data)

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
