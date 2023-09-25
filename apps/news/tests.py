from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.news.models import Category, News, Tag


class NewsListAPITestCase(APITestCase):
    def test_news_list(self):
        response = self.client.get(reverse("news"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class NewsDetailAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testuser")
        self.news = News.objects.create(title="Testnews", author=self.user)

    def test_news_detail_endpoint(self):
        url = reverse("news_detail", kwargs={"slug": self.news.slug})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
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


class RecommendNewsAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testuser")
        self.tag = Tag.objects.create(name="TestTag")
        self.news_1 = News.objects.create(title="News 1", content="Content 1", author=self.user, is_recommended=True)
        self.news_2 = News.objects.create(title="News 2", content="Content 2", author=self.user, is_recommended=True)
        self.news_3 = News.objects.create(title="News 3", content="Content 3", author=self.user)
        self.news_1.tag.add(self.tag)
        self.news_2.tag.add(self.tag)

    def test_recommend_news_endpoint(self):
        url = reverse("recommend_news", kwargs={"tag": self.tag.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)
        self.assertEqual(response.data["results"][0]["title"], self.news_1.title)
