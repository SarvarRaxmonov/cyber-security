from django.urls import path

from apps.news.views import (CategoryNewsAPIView, NewsDetailAPIView,
                             NewsListAPIView, RecommendNewsAPIView)

urlpatterns = [
    path("", NewsListAPIView.as_view(), name="news"),
    path("<slug:slug>/", NewsDetailAPIView.as_view(), name="news_detail"),
    path("category/<int:pk>/", CategoryNewsAPIView.as_view(), name="category_news"),
    path("recommend/<int:tag>/", RecommendNewsAPIView.as_view(), name="recommend_news"),
]
