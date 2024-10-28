from django.contrib import admin
from .models import Showtime, Ticket, Payment, Discount


@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'screen', 'show_time', 'ticket_price']


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'showtime', 'seat_number', 'is_paid']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'ticket', 'amount', 'payment_status', 'payment_date']

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'percent', 'start_time', 'end_time', 'max_usage', 'times_used', 'is_active')
    filter_horizontal = ('users', 'showtime')