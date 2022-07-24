from datetime import datetime

from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView,DestroyAPIView

from .models import Booking, Flight
from .serializers import BookingListSerializer, DetailSerializer,UpdateSerializer, FlightListSerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer
    
class BookingAPIView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class= DetailSerializer
    lookup_field="id"
    lookup_url_kwarg="booking_id"
    
    
class BookingUpdateAPIView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class= UpdateSerializer
    lookup_field="id"
    lookup_url_kwarg="booking_id"
    
class BookingDeleteAPIView(DestroyAPIView):
    queryset = Booking.objects.all()
    
    lookup_field="id"
    lookup_url_kwarg="booking_id"
