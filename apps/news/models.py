import uuid

from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextChoices


class News(models.Model):
    class NewsTypes(TextChoices):
        NEWS = "news", "News"
        ARTICLE = "article", "Article"

    class StatusChoices(TextChoices):
        MODERATION = "moderation", "Moderation"
        PUBLISHED = "published", "Published"
        ARCHIVED = "archived", "Archived"

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", unique=True, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField("Category")
    content = RichTextUploadingField(blank=True, null=True)
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=NewsTypes.choices, blank=True, null=True)
    is_recommended = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, blank=True, null=True)
    tag = models.ManyToManyField("Tag")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NewsView(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="views")
    device_id = models.UUIDField(default=uuid.uuid4, editable=False)


class Category(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)
