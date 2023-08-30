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
    content = RichTextUploadingField()
    cover = models.ImageField(upload_to="covers/")
    description = RichTextField()
    type = models.CharField(max_length=20, choices=NewsTypes.choices)
    is_recommended = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=StatusChoices.choices)
    tag = models.ManyToManyField("Tag")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NewsView(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    device_id = models.UUIDField(default=uuid.uuid4, editable=False)


class Category(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)
