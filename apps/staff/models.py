from ckeditor.fields import RichTextField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Models
class Center(models.Model):
    name = models.CharField(max_length=100)


class Department(models.Model):
    name = models.CharField(max_length=100)
    center = models.ForeignKey(Center, on_delete=models.CASCADE)


class SubDepartment(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Position(models.Model):
    name = models.CharField(max_length=100)
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    sub_department = models.ForeignKey(SubDepartment, on_delete=models.CASCADE)


class Responsibility(models.Model):
    class ResponsibilityType(models.TextChoices):
        POSITION = "position", "Position"
        DEPARTMENT = "department", "Department"
        COMPANY = "company", "Company"

    text = RichTextField()
    type = models.CharField(max_length=20, choices=ResponsibilityType.choices)


class WorkingType(models.Model):
    name = models.CharField(max_length=100)


class CenterManagement(models.Model):
    fullname = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    phone_number = PhoneNumberField()
    email = models.EmailField()
    working_time = models.CharField(max_length=200)
    responsibility = models.ManyToManyField(Responsibility)
    biography = RichTextField()
    officials = models.ManyToManyField("self", symmetrical=False,blank=True)


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    icon = models.FileField(upload_to="icons/")
    salary_type = models.ForeignKey(WorkingType, on_delete=models.CASCADE)
    salary_from = models.DecimalField(max_digits=10, decimal_places=2)
    salary_to = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    description = models.TextField()


class VacancyView(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    device_id = models.UUIDField(editable=False)


class Resume(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    file = models.FileField(upload_to="resumes/")
