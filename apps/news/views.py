from rest_framework import generics
from apps.news.serializers import MainNewsSerializer, CategoryNewsSerializer
from apps.news.models import News


class NewsListAPIView(generics.ListAPIView):
    serializer_class = MainNewsSerializer
    queryset = News.objects.all()


class CategoryNewsAPIView(generics.ListAPIView):
    serializer_class = CategoryNewsSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk", None)
        return News.objects.filter(category=pk)

