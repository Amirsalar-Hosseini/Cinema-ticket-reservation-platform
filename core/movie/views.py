from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from .models import Movie, Review, Genre
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated


class MovieView(APIView):
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request):
        genres = request.query_params.getlist('genres', None)
        movies = self.queryset.all()
        if genres:
            genres_name = Genre.objects.filter(name__in=genres)
            movies = movies.filter(genre__in=genres_name).distinct()
        paginator = self.pagination_class()
        paginator.page_size = 10
        paginated_movies = paginator.paginate_queryset(movies, request)
        ser_data = self.serializer_class(paginated_movies, many=True)
        return paginator.get_paginated_response(ser_data.data)

class MovieDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, pk):
        movie = self.queryset.get(pk=pk)
        ser_data = self.serializer_class(movie)
        return Response(ser_data.data)

    def post(self, request, pk):
        rating = request.data.get('rating')
        comment = request.data.get('comment')
        movie = Movie.objects.get(pk=pk)
        user = User.objects.get(id=request.user.id)
        Review.objects.create(user=user, rating=rating, comment=comment, movie=movie)
        return Response({'SUCCESS': 'thanks for comment'}, status=status.HTTP_201_CREATED)

