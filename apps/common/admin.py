from django.contrib import admin

from .models import (Category, Document, GetHackedReport, Message, Service,
                     Site, Tag)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "icon")
    search_fields = ("name",)


@admin.register(GetHackedReport)
class GetHackedReportAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "site")
    search_fields = ("phone_number", "site")


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ("type", "icon", "url", "description")
    list_filter = ("type",)
    search_fields = ("url",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "number_order", "created_at", "updated_at")
    list_filter = ("category",)
    search_fields = ("name", "category__name", "number_order")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("fullname", "phone_number", "text", "type")
    search_fields = ("type", "phone_number")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
