from django.db import models
from accounts.models import User
from cinema.models import Screen
from movie.models import Movie


class Showtime(models.Model):
    """
    movie play time at specific location
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    price_category = models.ForeignKey('PriceCategory', on_delete=models.CASCADE)
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
    is_paid = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'Ticket for {self.showtime.movie.title} at {self.showtime.show_time} for seat {self.seat_number}'


class Reservation(models.Model):
    """
    reserve info for Admin
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    num_of_tickets = models.IntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    reserved_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'Reservation by {self.user.first_name} {self.user.last_name} for {self.num_of_tickets} tickets'


class Payment(models.Model):
    """
    payment info
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment of {self.amount} by {self.user.first_name} {self.user.last_name} for {self.reservation.id}'

class PriceCategory(models.Model):
    """
    define category for price
    """
    price_range = models.CharField(max_length=50)
    min_price = models.DecimalField(max_digits=6, decimal_places=2)
    max_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.price_range} {self.min_price} - {self.max_price}'