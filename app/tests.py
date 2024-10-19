from django.test import TestCase, Client
from django.urls import reverse
from .models import Menu, Booking, Rating
from django.contrib.auth.models import User
from datetime import datetime

# app/test_views.py


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.menu_item = Menu.objects.create(name='Test Item', price=30)
        self.booking = Booking.objects.create(
            first_name='Test',
            reservation_date=datetime.today().date(),
            reservation_slot='10'
        )
        self.rating = Rating.objects.create(rating=5, menu=self.menu_item)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_reservations_view(self):
        response = self.client.get(reverse('reservations'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings.html')

    def test_book_view_get(self):
        response = self.client.get(reverse('book'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book.html')

    def test_book_view_post(self):
        response = self.client.post(reverse('book'), {
            'first_name': 'Test',
            'reservation_date': datetime.today().date(),
            'reservation_slot': '10'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book.html')

    def test_menu_view(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

    def test_display_menu_item_view(self):
        response = self.client.get(reverse('menu_item', args=[self.menu_item.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu_item.html')

    def test_bookings_view_post(self):
        response = self.client.post(reverse('bookings'), {
            'first_name': 'Test',
            'reservation_date': datetime.today().date(),
            'reservation_slot': '10'
        }, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_rating_view_post(self):
        response = self.client.post(reverse('rating'), {
            'menu_id': self.menu_item.pk,
            'rating': 5
        }, content_type='application/json')
        self.assertEqual(response.status_code, 302)

    def test_user_view_post(self):
        response = self.client.post(reverse('user'), {
            'username': 'newuser',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user.html')

    def test_login_view_post(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')