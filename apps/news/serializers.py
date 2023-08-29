from rest_framework import serializers

from .models import Category, News, NewsView, Tag


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "title",
            "author",
            "category",
            "content",
            "cover",
            "description",
            "type",
            "is_recommended",
            "status",
            "tag",
            "created_at",
            "updated_at",
        )


class NewsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsView
        fields = ("news", "device_id")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)
