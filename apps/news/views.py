from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from apps.news.models import News
from apps.news.serializers import (
    CategoryNewsSerializer,
    MainNewsSerializer,
    NewsSerializer,
    RecommendNewsSerializer
)

class NewsListAPIView(generics.ListAPIView):
    serializer_class = MainNewsSerializer
    queryset = News.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["title"]
    search_fields = ["title"]


class CategoryNewsAPIView(generics.ListAPIView):
    serializer_class = CategoryNewsSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk", None)
        return News.objects.filter(category=pk)


class NewsDetailAPIView(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        slug = self.kwargs.get("slug", None)
        return News.objects.filter(slug=slug)


class RecommendNewsAPIView(generics.ListAPIView):
    serializer_class = RecommendNewsSerializer

    def get_queryset(self):
        tag = self.kwargs.get("tag", None)
        return News.objects.filter(is_recommended=True, tag=tag)
