from django.contrib import admin

from .models import (
    Center,
    CenterManagement,
    Department,
    Position,
    Responsibility,
    Resume,
    SubDepartment,
    Vacancy,
    VacancyView,
    WorkingType,
)


@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "center")
    list_filter = ("center",)
    search_fields = ("name",)


@admin.register(SubDepartment)
class SubDepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "department")
    list_filter = ("department",)
    search_fields = ("name",)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name", "center", "department", "sub_department")
    list_filter = ("center", "department", "sub_department")
    search_fields = ("name",)


@admin.register(Responsibility)
class ResponsibilityAdmin(admin.ModelAdmin):
    list_display = ("text", "type")
    list_filter = ("type",)
    search_fields = ("text",)


@admin.register(WorkingType)
class WorkingTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(CenterManagement)
class CenterManagementAdmin(admin.ModelAdmin):
    list_display = ("fullname", "position", "email")
    list_filter = ("position", "officials")
    search_fields = ("fullname", "email")


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "salary_type", "salary_from", "salary_to")
    list_filter = ("salary_type",)
    search_fields = ("title", "company")


@admin.register(VacancyView)
class VacancyViewAdmin(admin.ModelAdmin):
    list_display = ("vacancy", "device_id")
    search_fields = ("vacancy__title", "device_id")


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("vacancy", "phone_number")
    search_fields = ("vacancy__title", "phone_number")
