from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class HomeViewTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_home_redirects_when_not_logged_in(self):
        """
        If the user is not logged in, home should redirect to the login page.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)  # Ensures it redirects to login

    def test_home_loads_for_logged_in_user(self):
        """
        Logged-in users should be able to access the home page.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.c
