# Generated by Django 4.2.4 on 2023-08-30 07:43

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                blank=True,
                editable=False,
                null=True,
                populate_from="title",
                unique=True,
            ),
        ),
    ]
