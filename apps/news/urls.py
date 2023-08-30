from django.urls import path

from apps.news.views import CategoryNewsAPIView, NewsListAPIView

urlpatterns = [path("", NewsListAPIView.as_view(), name="news"), path("category/<int:pk>/", CategoryNewsAPIView.as_view(), name="category_news")]
