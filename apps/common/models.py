from django.core.exceptions import ValidationError
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.FileField(upload_to="icons/")

    def __str__(self):
        return self.name


class GetHackedReport(models.Model):
    phone_number = PhoneNumberField()
    site = models.URLField()

    def __str__(self):
        return self.site


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

    def __str__(self):
        return self.url


class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    file = models.FileField(upload_to="documents/", blank=True)
    url = models.URLField(blank=True)
    number_order = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def clean(self):
        if not self.url and not self.file:
            raise ValidationError("Please choose a file to upload or indicate url ")


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Message(models.Model):
    class Types(models.TextChoices):
        QUESTION = "question", "Question"
        CONTACT = "contact", "Contact"

    fullname = models.CharField(max_length=100)
    type = models.CharField(
        max_length=20,
        choices=Types.choices,
        default=Types.QUESTION,
    )
    phone_number = PhoneNumberField()
    text = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.fullname
