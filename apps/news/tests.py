from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase 
from apps.news.models import Category, News, Tag

from .views import NewsListAPIView


class NewsListAPITestCase(APITestCase):
    def test_news_list(self):
        response = self.client.get(reverse("news"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class NewsDetailAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testuser")
        # self.category = Category.objects.create(name="TestCategory")
        # self.tag = Tag.objects.create(name="TestTag")
        self.news = News.objects.create(title="Testnews", author=self.user)

    def test_news_detail_endpoint(self):
        url = reverse("news_detail", kwargs={"slug": self.news.slug})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["title"], self.news.title)
        self.assertEqual(response.data["results"][0]["slug"], self.news.slug)
        self.assertEqual(response.wsgi_request.user, self.user)


class CategoryNewsAPITestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="TestCategory")
        self.user = User.objects.create_user(username="testuser", password="testuser")
        self.news = News.objects.create(title="Testnews", author=self.user)
        self.news.category.set([self.category])

    def test_category_news_endpoint(self):
        url = reverse("category_news", kwargs={"pk": self.category.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        category_ids = response.data["results"][0]["category"]
        self.assertIn(self.category.id, category_ids)
