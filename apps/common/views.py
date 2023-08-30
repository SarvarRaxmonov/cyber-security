import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Category, Document, GetHackedReport, Message, Service, Site, Tag
from .serializers import (
    CategorySerializer,
    DocumentSerializer,
    GetHackedReportSerializer,
    MessageSerializer,
    ServiceSerializer,
    SiteSerializer,
    TagSerializer,
)


class SiteListView(generics.ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class ServiceListView(generics.RetrieveAPIView, generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "pk"

    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            return self.retrieve(request, pk, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)


class GetHackedCreateView(generics.CreateAPIView):
    queryset = GetHackedReport.objects.all()
    serializer_class = GetHackedReportSerializer


class DocumentListView(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentCategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MessageTagsListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class MessageCreateView(generics.CreateAPIView):
    queryset = None
    serializer_class = MessageSerializer


class MessageFilter(django_filters.FilterSet):
    tag = django_filters.CharFilter(field_name="tags__name", lookup_expr="iexact")

    class Meta:
        model = Message
        fields = ("tag",)


class FrequentAskedQuestionsListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter

    def get_queryset(self):
        return Message.objects.exclude(tags=None)
