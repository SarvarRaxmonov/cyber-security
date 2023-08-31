from django.contrib import admin

from .models import Category, News, NewsView, Tag


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "slug",
        "type",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = ("type", "status", "created_at", "updated_at")
    search_fields = ("title", "author__username")


@admin.register(NewsView)
class NewsViewAdmin(admin.ModelAdmin):
    list_display = ("news", "device_id")
    search_fields = ("news__title", "device_id")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
