from rest_framework import serializers

from .models import (Center, CenterManagement, Department, Position,
                     Responsibility, Resume, SubDepartment, Vacancy,
                     VacancyView, WorkingType)

# ----------------------------------------------------------------


class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ("name",)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ("name", "center")


class SubDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDepartment
        fields = ("name", "department")


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ("name", "center", "department", "sub_department")


class ResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsibility
        fields = ("text", "type")


class WorkingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingType
        fields = ("name",)


class CenterManagementSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    responsibility = ResponsibilitySerializer(many=True)
    officials = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CenterManagement
        fields = (
            "fullname",
            "position",
            "image",
            "phone_number",
            "email",
            "working_time",
            "responsibility",
            "biography",
            "officials",
        )


class VacancySerializer(serializers.ModelSerializer):
    salary_type = WorkingTypeSerializer()
    salary_from = serializers.DecimalField(max_digits=10, decimal_places=2)
    salary_to = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Vacancy
        fields = (
            "title",
            "company",
            "icon",
            "salary_type",
            "salary_from",
            "salary_to",
            "location",
            "phone_number",
            "description",
        )


class VacancyViewSerializer(serializers.ModelSerializer):
    vacancy = VacancySerializer()

    class Meta:
        model = VacancyView
        fields = ("vacancy", "device_id")


class ResumeSerializer(serializers.ModelSerializer):
    vacancy = VacancySerializer()

    class Meta:
        model = Resume
        fields = ("vacancy", "phone_number", "file")
