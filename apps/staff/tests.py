from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.staff.models import Position, Center, Department, SubDepartment, Responsibility


class StaffTestCase(APITestCase):
    def setUp(self):
        self.center = Center.objects.create(name='Center 1')
        self.department = Department.objects.create(name='Dep 1', center=self.center)
        self.sub_department = SubDepartment.objects.create(
            name='Sub Department 1', department=self.department
        )
        self.position = Position.objects.create(
            name='Position 1',
            center=self.center,
            department=self.department,
            sub_department=self.sub_department
        )
        self.responsibility = Responsibility.objects.create(
            text='<p>asdas</p>',
            type='company'
        )

