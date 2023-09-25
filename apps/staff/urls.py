from django.urls import path

from apps.staff.views import (CenterManagementListAPIView,
                              CenterManagementRetrieveAPIView,
                              ResumeRetrieveAPIView, VacancyListAPIView,
                              VacancyRetrieveAPIView)

urlpatterns = [
    path("manager/list/", CenterManagementListAPIView.as_view(), name="manager_list"),
    path(
        "manager/<int:pk>/detail/",
        CenterManagementRetrieveAPIView.as_view(),
        name="manager_detail",
    ),
    path("resume/create/", ResumeRetrieveAPIView.as_view(), name="resume_create"),
    path("vacancy/list/", VacancyListAPIView.as_view(), name="vacancy_list"),
    path(
        "vacancy/<int:pk>/detail/",
        VacancyRetrieveAPIView.as_view(),
        name="vacancy_detail",
    ),
]
