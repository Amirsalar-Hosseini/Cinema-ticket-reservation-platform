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
    num_of_tickets = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'Ticket for {self.showtime.movie.title} at {self.showtime.show_time} for seat {self.seat_number}'


class Payment(models.Model):
    """
    payment info
    """


    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('cash', 'Cash'),
        ('wallet', 'Wallet'),
        ('cryptocurrency', 'Cryptocurrency'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=50, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment of {self.amount} by {self.user.first_name} {self.user.last_name} for {self.ticket.id}'
