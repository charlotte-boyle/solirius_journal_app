from django.test import TestCase
from django.urls import reverse
import pytest


class RouteTest(TestCase):
    @pytest.mark.django_db
    def test_homepage(self):
        homepage_url = reverse('journal:home')
        response = self.client.get(homepage_url)
        assert response.status_code == 200
