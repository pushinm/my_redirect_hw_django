from django.urls import path

from teachers.urls import app_name

from .views import subjects_view, subjects_delete, change_teacher
# from classboard.views import filter_students_group

app_name = 'subjects'

urlpatterns = [
    path('', subjects_view, name='subjects_view'),
    path('<int:pk>/', subjects_view, name='subjects_view'),
    path('delete/<int:pk>/', subjects_delete, name='subjects_delete'),
    # path('with_teacher/', show_classes_teacher, name='show_classes_teacher'),
    # path('with_teacher/<int:pk>', show_classes_teacher, name='show_classes_teacher'),
    # path('with_teacher', class_view, name='class_view'),
    path('change_teacher/<int:pk>/<int:tpk>', change_teacher, name='change_teacher'),
    # path('filter_group/', filter_students_group, name='filter_students_group'),
]
