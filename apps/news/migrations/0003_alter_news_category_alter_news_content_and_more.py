# Generated by Django 4.2.4 on 2023-08-30 09:18

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_news_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="category",
            field=models.ManyToManyField(blank=True, null=True, to="news.category"),
        ),
        migrations.AlterField(
            model_name="news",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="cover",
            field=models.ImageField(blank=True, null=True, upload_to="covers/"),
        ),
        migrations.AlterField(
            model_name="news",
            name="description",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="news",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("moderation", "Moderation"),
                    ("published", "Published"),
                    ("archived", "Archived"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="tag",
            field=models.ManyToManyField(blank=True, null=True, to="news.tag"),
        ),
        migrations.AlterField(
            model_name="news",
            name="type",
            field=models.CharField(
                blank=True,
                choices=[("news", "News"), ("article", "Article")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="newsview",
            name="news",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="views",
                to="news.news",
            ),
        ),
    ]
