from rest_framework import serializers

from .models import (Category, Document, GetHackedReport, Message, Service,
                     Site, Tag)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("name", "description", "icon")


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ("type", "icon", "url", "description")


class GetHackedReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetHackedReport
        fields = ("phone_number", "site")


class DocumentSerializer(serializers.ModelSerializer):
    file_size = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = (
            "name",
            "category",
            "description",
            "file",
            "url",
            "file_size",
            "number_order",
            "created_at",
            "updated_at",
        )

    def get_file_size(self, obj):
        if obj.file:
            return self.get_human_readable_size(obj.file.size)
        return None

    def get_human_readable_size(self, size_in_bytes):
        units = ["B", "KB", "MB", "GB", "TB"]
        size = size_in_bytes
        unit_index = 0

        while size >= 1024 and unit_index < len(units) - 1:
            size /= 1024.0
            unit_index += 1

        return "{:.2f} {}".format(size, units[unit_index])


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)


class MessageSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Message
        fields = ("fullname", "phone_number", "type", "text", "tags")
