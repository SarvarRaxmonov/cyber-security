from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Site


class SiteListViewTest(APITestCase):
    def setUp(self):
        self.site1 = Site.objects.create(type="partner", url="http://example.com", description="Partner site")
        self.site2 = Site.objects.create(type="resource", url="http://example.org", description="Resource site")
        self.site2 = Site.objects.create(type="our company", url="http://example.org", description="Resource site")
        self.url = reverse("site-list")

    def test_list_sites(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 3)
