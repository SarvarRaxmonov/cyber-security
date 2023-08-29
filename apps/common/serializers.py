from rest_framework import serializers

from .models import Document, GetHackedReport, Message, Service, Site


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("name", "description", "icon")


class GetHackedReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetHackedReport
        fields = ("phone_number", "site")


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ("types", "icon", "url", "description")


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            "name",
            "category",
            "description",
            "file",
            "url",
            "number_order",
            "created_at",
            "updated_at",
        )


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("fullname", "phone_number", "text")
