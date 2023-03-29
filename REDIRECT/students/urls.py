from django.urls import path
from .views import (
    StudentAddView,
    StudentTempateView,
    StudentDeleteView,
    StudentUpdateView,
    StudentListView
)


urlpatterns = [
    path("", StudentListView.as_view(), name="students_view"),
    path("<int:pk>/", StudentTempateView.as_view(), name="students_view"),
    path("add", StudentAddView.as_view(), name="student_add"),
    path("<int:pk>/update/", StudentUpdateView.as_view(), name="student_update"),
    path("<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"),
]
