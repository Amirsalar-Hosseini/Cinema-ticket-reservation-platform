from decimal import Decimal
from django.db import models
from accounts.models import User
from cinema.models import Screen
from movie.models import Movie
from django.utils import timezone


class Showtime(models.Model):
    """
    movie play time at specific location
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    show_time = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.movie.title} at {self.show_time} on Screen {self.screen.screen_number}'


class Ticket(models.Model):
    """
    ticket info for User
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Ticket for {self.showtime.movie.title} at {self.showtime.show_time} for seat {self.seat_number}'

    class Meta:
        unique_together = ('showtime', 'seat_number')


class Payment(models.Model):
    """
    payment info
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_status = models.CharField(max_length=50, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment of {self.amount} by {self.user.first_name} {self.user.last_name} for {self.ticket.id}'


class Discount(models.Model):
    name = models.CharField(max_length=100, unique=True)
    discount_code = models.CharField(max_length=100, unique=True, null=True)
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    users = models.ManyToManyField(User, blank=True)
    showtime = models.ManyToManyField(Showtime, blank=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField()
    max_usage = models.PositiveIntegerField()
    times_used = models.PositiveIntegerField(default=0)

    def is_active(self):
        return self.start_time <= timezone.now() <= self.end_time and self.times_used < self.max_usage

    def __str__(self):
        return f"{self.name} - {self.percent}%"