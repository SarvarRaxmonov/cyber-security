from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category, Document, Service, Site, Tag


class SiteListViewTest(APITestCase):
    def setUp(self):
        self.site1 = Site.objects.create(
            type="partner", url="http://example.com", description="Partner site"
        )
        self.site2 = Site.objects.create(
            type="resource", url="http://example.org", description="Resource site"
        )
        self.site2 = Site.objects.create(
            type="our company", url="http://example.org", description="Resource site"
        )
        self.url = reverse("site-list")

    def test_list_sites(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 3)


class ServiceListViewTest(APITestCase):
    def setUp(self):
        self.service = Service.objects.create(
            name="partner", description="Partner site"
        )
        self.url = reverse("service-list")

    def test_list_services(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_detail_service(self):
        response = self.client.get(
            reverse("service-retrieve", kwargs={"pk": self.service.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.service.name)
        self.assertEqual(response.data["description"], self.service.description)


class GetHackedCreateViewTest(APITestCase):
    def setUp(self):
        self.report = {
            "phone_number": "+998946643023",
            "site": "https://pypi.org/project/django-filter/",
        }
        self.url = reverse("get-hacked")

    def test_list_services(self):
        response = self.client.post(self.url, data=self.report)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["phone_number"], self.report.get("phone_number"))
        self.assertEqual(response.data["site"], self.report.get("site"))


class DocumentListViewTest(APITestCase):
    def setUp(self):
        self.uploaded_file = SimpleUploadedFile(
            "test_file.txt", b"Test content for the file", content_type="text/plain"
        )
        self.category = Category.objects.create(name="nimadir")
        self.document = Document.objects.create(
            name="partner",
            category=self.category,
            file=self.uploaded_file,
            number_order="bb2323",
            description="Partner site",
        )
        self.url = reverse("documents-list")

    def test_list_documents(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_list_documents_categries(self):
        response = self.client.get(reverse("documents-categories-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)


class MessageTest(APITestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="tag1")

    def test_message_tags_list(self):
        url = reverse("message-tags-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    # def test_frequent_asked_questions_list(self):
    #
    #     obj = Message.objects.all()
    #     print(obj)
    #     url_2 = reverse("frequently_asked_questions_list")
    #     response = self.client.get(url_2)
    #     self.assertEqual(response.data["count"], 1)
