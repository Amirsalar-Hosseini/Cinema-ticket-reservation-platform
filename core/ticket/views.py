from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Showtime, Ticket, Payment
from .serializers import ShowtimeSerializer, TicketSerializer, PaymentSerializer


class ShowtimeView(APIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer

    def get(self, request):
        city = request.query_params.get('city', None)
        province = request.query_params.get('province', None)
        if not city or not province:
            return Response(data={'error': 'Both city and province are required'}, status=status.HTTP_400_BAD_REQUEST)

        showtimes = self.queryset.filter(screen__cinema__location__province=province, screen__cinema__location__city=city)
        if showtimes.exists():
            ser_data = self.serializer_class(showtimes, many=True)
            return Response(ser_data.data)
        else:
            return Response({'message': 'no showtime available'}, status=status.HTTP_404_NOT_FOUND)


class TicketView(APIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get(self, request):
        tickets = self.queryset.all()
        ser_data = self.serializer_class(tickets, many=True)
        return Response(ser_data.data)


class PaymentView(APIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get(self, request):
        payments = self.queryset.all()
        ser_data = self.serializer_class(payments, many=True)
        return Response(ser_data.data)