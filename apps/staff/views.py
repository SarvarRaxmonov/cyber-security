from rest_framework import generics

from apps.staff.models import CenterManagement, Vacancy, Resume
from apps.staff.serializers import CenterManagementSerializer, VacancySerializer, ResumeSerializer
from rest_framework.parsers import FormParser, MultiPartParser


class CenterManagementListAPIView(generics.ListAPIView):
    queryset = CenterManagement.objects.all()
    serializer_class = CenterManagementSerializer


class CenterManagementRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CenterManagement.objects.all()
    serializer_class = CenterManagementSerializer


class VacancyListAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class VacancyRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class ResumeRetrieveAPIView(generics.CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    parser_classes = (FormParser, MultiPartParser)
