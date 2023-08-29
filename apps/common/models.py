from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.FileField(upload_to="icons/")


class GetHackedReport(models.Model):
    phone_number = PhoneNumberField()
    site = models.URLField()


class Site(models.Model):
    class Types(models.TextChoices):
        PARTNER = "partner", "Partner"
        RESOURCE = "resource", "Resource"
        OUR_COMPANY = "our company", "Our Company"

    type = models.CharField(
        max_length=20,
        choices=Types.choices,
        default=Types.PARTNER,
    )
    icon = models.ImageField(upload_to="site_icons/")
    url = models.URLField()
    description = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=500)


class Document(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    file = models.FileField(upload_to="documents/")
    url = models.URLField()
    number_order = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    fullname = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    text = models.TextField()
