from django.urls import path
from .views import MovieView, MovieDetailView

app_name = 'movie'
urlpatterns = [
    path('', MovieView.as_view(), name='movie'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
]