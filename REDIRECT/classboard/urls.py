from django.urls import path
from .views import classboard_view

urlpatterns = [
    path('', classboard_view, name='classboard_view'),
    path('<int:pk>', classboard_view, name='classboard_view'),   
]
