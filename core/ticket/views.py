from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Showtime, Ticket, Payment
from .serializers import ShowtimeSerializer, TicketSerializer, PaymentSerializer
from accounts.models import User


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


class ShowTimeDetailView(APIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer

    def get(self, request, pk):
        showtime = self.queryset.get(pk=pk)
        ser_data = self.serializer_class(showtime)
        return Response(ser_data.data)


class TicketView(APIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get(self, request, showtime_id, *args, **kwargs):
        showtime = Showtime.objects.get(id=showtime_id)
        booked_seat_number = [ticket.seat_number for ticket in self.queryset.filter(showtime__id=showtime.id)]
        seat_numbers = [str(i) for i in range(1, showtime.screen.capacity + 1)]
        available_seats = sorted(list(set(seat_numbers) - set(booked_seat_number)))

        response_data = {
            'showtime_id': showtime.id,
            'seat_numbers': seat_numbers,
            'available_seat': available_seats,
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request, showtime_id, *args, **kwargs):
        showtime = Showtime.objects.get(id=showtime_id)
        user = User.objects.get(id=request.user.id)
        seat_number = request.data.get('seat_number')
        num_of_tickets = int(request.data.get('num_of_tickets'))
        if self.queryset.filter(showtime=showtime, seat_number=seat_number).exists():
            return Response({'error': 'this seat is already booked'}, status=status.HTTP_400_BAD_REQUEST)

        ticket = self.queryset.create(user=user, showtime=showtime, seat_number=seat_number, num_of_tickets=num_of_tickets)
        ticket.save()
        return Response({'success': 'ticket created successfully', "total_price": ticket.total_price}, status=status.HTTP_201_CREATED)



class PaymentView(APIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def post(self, request, ticket_id, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        ticket = Ticket.objects.get(id=ticket_id)
        amount = ticket.total_price
        payment_status = request.data.get('payment_status')
        if payment_status:
            payment_status = 'Success'
        else:
            payment_status = 'Failed'

        Payment.objects.create(user=user, ticket=ticket, amount=amount, payment_status=payment_status)

        return Response({'message': 'created successfully'})