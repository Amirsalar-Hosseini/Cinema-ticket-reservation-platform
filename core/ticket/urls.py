from django.urls import path
from .views import PaymentView, ShowtimeView, TicketView, ShowTimeDetailView

app_name = 'ticket'
urlpatterns = [
    path('', TicketView.as_view(), name='ticket'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('showtime/', ShowtimeView.as_view(), name='showtime'),
    path('showtime/<int:pk>/', ShowTimeDetailView.as_view(), name='showtime_detail'),
]