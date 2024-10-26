from django.db import models
from accounts.models import User

class Movie(models.Model):
    """
    define movie model
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text='duration in minutes')
    genre = models.ManyToManyField('Genre', blank=True)
    director = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    age_rating = models.CharField(max_length=10)
    poster = models.ImageField(upload_to=f'movie_posters/', blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    """
    define user comments
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews'   )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.first_name} {self.user.last_name} for {self.movie.title}'


class Genre(models.Model):
    """
    for genre category
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name