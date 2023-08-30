from apps.news.views import NewsListAPIView, CategoryNewsAPIView
from django.urls import path


urlpatterns = [
    path("", NewsListAPIView.as_view(), name="news"),
    path("category/<int:pk>/", CategoryNewsAPIView.as_view(), name="category_news")
]
