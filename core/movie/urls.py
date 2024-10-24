from django.urls import path
from .views import ReviewView, MovieView

app_name = 'movie'
urlpatterns = [
    path('', MovieView.as_view(), name='movie'),
    path('review/', ReviewView.as_view(), name='review'),
]