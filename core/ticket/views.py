from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Showtime, Ticket, Payment
from .serializers import ShowtimeSerializer, TicketSerializer, PaymentSerializer


class ShowtimeView(APIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer

    def get(self, request):
        showtimes = self.queryset.all()
        ser_data = self.serializer_class(showtimes, many=True)
        return Response(ser_data.data)


class TicketView(APIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get(self, request):
        tickets = self.queryset.all()
        ser_data = self.serializer_class(tickets, many=True)
        return Response(ser_data.data)


# class ReservationView(APIView):
#     queryset = Reservation.objects.all()
#     serializer_class = ReservationSerializer
#
#     def get(self, request):
#         reservations = self.queryset.all()
#         ser_data = self.serializer_class(reservations, many=True)
#         return Response(ser_data.data)


class PaymentView(APIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get(self, request):
        payments = self.queryset.all()
        ser_data = self.serializer_class(payments, many=True)
        return Response(ser_data.data)


# class PriceCategoryView(APIView):
#     queryset = PriceCategory.objects.all()
#     serializer_class = PriceCategorySerializer
#
#     def get(self, request):
#         price_categories = self.queryset.all()
#         ser_data = self.serializer_class(price_categories, many=True)
#         return Response(ser_data.data)
