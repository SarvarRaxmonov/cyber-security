from ckeditor.fields import RichTextField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Center(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Center'
        verbose_name_plural = 'Center'


class Department(models.Model):
    name = models.CharField(max_length=100)
    center = models.ForeignKey(Center, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class SubDepartment(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubDepartment'
        verbose_name_plural = 'SubDepartments'


class Position(models.Model):
    name = models.CharField(max_length=100)
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    sub_department = models.ForeignKey(SubDepartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'


class Responsibility(models.Model):
    class ResponsibilityType(models.TextChoices):
        POSITION = "position", "Position"
        DEPARTMENT = "department", "Department"
        COMPANY = "company", "Company"

    text = RichTextField()
    type = models.CharField(max_length=20, choices=ResponsibilityType.choices)

    def __str__(self):
        return self.text[:11]

    class Meta:
        verbose_name = 'Responsibility'
        verbose_name_plural = 'Responsibilities'


class WorkingType(models.Model):
    name = models.CharField(max_length=100)


class SocialMedia(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SocialMedia'
        verbose_name_plural = 'SocialMedias'


class CenterManagement(models.Model):
    fullname = models.CharField(max_length=125)
    address = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    phone_number = PhoneNumberField()
    email = models.EmailField()
    working_time = models.CharField(max_length=255)
    responsibility = models.ManyToManyField(Responsibility)
    social_medias = models.ManyToManyField(SocialMedia)
    biography = RichTextField()
    officials = models.ManyToManyField("self", symmetrical=False, blank=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'CenterManagement'
        verbose_name_plural = 'CenterManagements'



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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'


class VacancyView(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    device_id = models.UUIDField(editable=False)

    def __str__(self):
        return self.vacancy.title

    class Meta:
        verbose_name = 'VacancyView'
        verbose_name_plural = 'VacancyViews'


class Resume(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    file = models.FileField(upload_to="resumes/")

    def __str__(self):
        return self.vacancy.title

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'
