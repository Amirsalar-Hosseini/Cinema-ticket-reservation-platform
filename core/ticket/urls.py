from django.urls import path
from .views import PaymentView, ShowtimeView, TicketView, ShowTimeDetailView

app_name = 'ticket'
urlpatterns = [
    path('<int:showtime_id>/', TicketView.as_view(), name='ticket'),
    path('payment/<int:ticket_id>/', PaymentView.as_view(), name='payment'),
    path('showtime/', ShowtimeView.as_view(), name='showtime'),
    path('showtime/<int:pk>/', ShowTimeDetailView.as_view(), name='showtime_detail'),
]