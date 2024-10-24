from django.urls import path
from .views import PaymentView, ShowtimeView, TicketView

app_name = 'ticket'
urlpatterns = [
    path('', TicketView.as_view(), name='ticket'),
    path('payment/', PaymentView.as_view(), name='payment'),
    # path('reservation/', ReservationView.as_view(), name='reservation'),
    path('showtime/', ShowtimeView.as_view(), name='showtime'),
    # path('pricecategory/', PriceCategoryView.as_view(), name='pricecategory'),
]