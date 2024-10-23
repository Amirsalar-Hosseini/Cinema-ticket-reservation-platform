from django.contrib import admin
from django.templatetags.i18n import language

from .models import Movie, Review, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_date', 'director', 'language', 'age_rating']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'user', 'rating', 'comment', 'created_at']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']