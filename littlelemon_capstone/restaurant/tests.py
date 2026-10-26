from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import MenuItem, Booking

class MenuAPITests(APITestCase):
    def test_menu_list_is_public(self):
        MenuItem.objects.create(title="Greek Salad", price="12.50", inventory=10)
        response = self.client.get("/api/menu/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Pagination wraps records in a results list.
        self.assertEqual(response.data["results"][0]["title"], "Greek Salad")

    def test_authenticated_user_can_create_menu_item(self):
        user = get_user_model().objects.create_user(username="tester", password="strongpass123")
        self.client.force_authenticate(user=user)
        response = self.client.post("/api/menu/", {"title":"Pasta", "price":"15.00", "inventory":5}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class BookingAPITests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="booker", password="strongpass123")
        self.client.force_authenticate(user=self.user)

    def test_authenticated_user_can_create_booking(self):
        response = self.client.post("/api/bookings/", {
            "name":"Sam", "no_of_guests":2, "booking_date":"2030-01-01T19:00:00Z"
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)

    def test_user_only_sees_own_bookings(self):
        other = get_user_model().objects.create_user(username="other", password="strongpass123")
        Booking.objects.create(name="Other", no_of_guests=2, booking_date="2030-01-01T19:00:00Z", user=other)
        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)

class RegistrationTests(APITestCase):
    def test_register_creates_user_and_token(self):
        response = self.client.post("/api/register/", {
            "username":"newuser", "email":"new@example.com", "password":"strongpass123"
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("token", response.data)
