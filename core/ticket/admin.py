from django.contrib import admin
from .models import Showtime, Ticket, Payment


@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'screen', 'show_time', 'ticket_price']


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'showtime', 'seat_number', 'num_of_tickets', 'is_paid', 'total_price']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'ticket', 'amount', 'payment_status', 'payment_date']