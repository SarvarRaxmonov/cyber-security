from django.urls import path

from .views import (
    DocumentCategoryListView,
    DocumentListView,
    FrequentAskedQuestionsListView,
    GetHackedCreateView,
    MessageCreateView,
    MessageTagsListView,
    ServiceListView,
    SiteListView,
)

urlpatterns = [
    path("sites/", SiteListView.as_view(), name="site-list"),
    path("services/", ServiceListView.as_view(), name="service-list"),
    path("service/<int:pk>/", ServiceListView.as_view(), name="service-retrieve"),
    path("get_hacked/", GetHackedCreateView.as_view(), name="get-hacked"),
    path("documents/", DocumentListView.as_view(), name="documents-list"),
    path(
        "documents_categories_list/",
        DocumentCategoryListView.as_view(),
        name="documents-categories-list",
    ),
    path("message/", MessageCreateView.as_view(), name="message"),
    path(
        "frequently_asked_questions_list/",
        FrequentAskedQuestionsListView.as_view(),
        name="frequently_asked_questions_list",
    ),
    path("message_tags_list/", MessageTagsListView.as_view(), name="message-tags-list"),
]
