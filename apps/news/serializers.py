from rest_framework import serializers

from .models import Category, News, NewsView, Tag


class MainNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "title",
            "cover",
            "created_at",
            "updated_at",
        )


class CategoryNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "title",
            "cover",
            "category",
            "created_at",
            "updated_at",
        )


class NewsSerializer(serializers.ModelSerializer):
    views_count = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = (
            "title",
            "slug",
            "author",
            "category",
            "content",
            "cover",
            "description",
            "type",
            "is_recommended",
            "status",
            "tag",
            "views_count",
            "created_at",
            "updated_at",
        )

    def get_views_count(self, obj):
        return obj.views.count()


class RecommendNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "title",
            "cover",
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
