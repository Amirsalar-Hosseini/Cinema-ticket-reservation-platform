from django.contrib import admin
from .models import Showtime, Ticket, Payment


@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'screen', 'show_time', 'ticket_price']


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'showtime', 'seat_number', 'num_of_tickets', 'is_paid', 'total_price']


# @admin.register(Reservation)
# class ReservationAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'showtime', 'num_of_tickets', 'total_price', 'reserved_at', 'is_confirmed']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'ticket', 'amount', 'payment_method', 'payment_status', 'payment_date']


# @admin.register(PriceCategory)
# class PriceCategoryAdmin(admin.ModelAdmin):
#     list_display = ['id', 'price_range', 'min_price', 'max_price']