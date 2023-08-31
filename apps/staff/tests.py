from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.staff.models import (Center, CenterManagement, Department, Position,
                               Responsibility, SubDepartment, Vacancy,
                               WorkingType)


class StaffTestCase(APITestCase):
    def setUp(self):
        # Set_Up for CenterManagement
        self.center = Center.objects.create(name="Center 1")
        self.department = Department.objects.create(name="Dep 1", center=self.center)
        self.sub_department = SubDepartment.objects.create(name="Sub Department 1", department=self.department)
        self.position = Position.objects.create(
            name="Position 1",
            center=self.center,
            department=self.department,
            sub_department=self.sub_department,
        )
        self.responsibility1 = Responsibility.objects.create(text="<p>asdas</p>", type="company")
        self.responsibility2 = Responsibility.objects.create(text="<p>asdas</p>", type="company")
        self.CenterManagement = CenterManagement.objects.create(
            fullname="qwerty",
            position=self.position,
            image="image.png",
            phone_number="+998974436638",
            email="test@gmail.com",
            working_time="qwer",
            # responsibility=/,
            biography="eqww",
        )

        # Set_Up for Vacancy
        self.work_type = WorkingType.objects.create(name="Full Time")
        self.vacancy = Vacancy.objects.create(
            title="title",
            company="company",
            icon="icon.png",
            salary_type=self.work_type,
            salary_from=1212.21,
            salary_to=12123.12,
            location="adasd",
            phone_number="+998974436638",
            description="qwerty",
        )

    def test_management_list(self):
        response = self.client.get(reverse("manager_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_management_detail(self):
        response = self.client.get(reverse("manager_detail", args=(self.CenterManagement.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vacancy_list(self):
        response = self.client.get(reverse("vacancy_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vacancy_detail(self):
        response = self.client.get(reverse("vacancy_detail", args=(self.CenterManagement.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_resume_create(self):
        self.uploaded_file = SimpleUploadedFile("test_file.txt", b"Test content for the file", content_type="text/plain")

        data = {
            "vacancy": self.vacancy.id,
            "phone_number": "+998974436638",
            "file": self.uploaded_file,
        }
        response = self.client.post(reverse("resume_create"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
