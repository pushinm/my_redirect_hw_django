from django.urls import path
from .views import (
    TestimonquialCreateView,
    TestimonialUpdateView,
    TestimonialDeleteView,
    TestimonialListViews,
    My_redirect_view,

)
from icecream import ic

app_name = "testimonials"

urlpatterns = [
    path("", TestimonialListViews.as_view(), name="testimonials_list"),
    path('<str:path>', My_redirect_view.as_view(), name='my_redirect'),
    path("create/", TestimonquialCreateView.as_view(), name="testimonials_create"),
    path(
        "<int:pk>/update/", TestimonialUpdateView.as_view(), name="testimonials_update"
    ),
    path(
        "<int:pk>/delete/", TestimonialDeleteView.as_view(), name="testimonials_delete"
    )
]
