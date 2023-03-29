from django.urls import path
from .views import show_mainpage, MainpageView

app_name = "mainpage"

urlpatterns = [
    path("", MainpageView.as_view(), name="mainpage"),
]
