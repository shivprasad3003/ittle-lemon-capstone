from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer, RegistrationSerializer

def home(request):
    return render(request, "restaurant/index.html")

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all().order_by("id")
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        # Authenticated users see their own bookings; staff can review all bookings.
        if self.request.user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RegisterView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        username = request.data.get("username")
        from django.contrib.auth import get_user_model
        user = get_user_model().objects.get(username=username)
        token, _ = Token.objects.get_or_create(user=user)
        response.data["token"] = token.key
        return response

class CurrentUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response({"id": request.user.id, "username": request.user.username, "email": request.user.email})
