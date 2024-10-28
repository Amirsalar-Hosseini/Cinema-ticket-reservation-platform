from django.db import models


class Cinema(models.Model):
    """
    define cinema model
    """
    name = models.CharField(max_length=200)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    address = models.TextField()
    num_of_screens = models.IntegerField()
    total_capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Screen(models.Model):
    """
    screen model for each Cinema
    """
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='screens')
    screen_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f'screen {self.screen_number} at {self.cinema.name}'

class Location(models.Model):
    """
    define location for cinema
    """
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.city} {self.province}'