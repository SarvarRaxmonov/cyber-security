# Generated by Django 4.2.4 on 2023-08-31 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_alter_news_category_alter_news_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="category",
            field=models.ManyToManyField(to="news.category"),
        ),
        migrations.AlterField(
            model_name="news",
            name="tag",
            field=models.ManyToManyField(to="news.tag"),
        ),
    ]
