from django.urls import path
from wages.views import show_teachers_grid, wage_recalculate

app_name = 'wages'

urlpatterns = [
    path('', show_teachers_grid, name='show_teachers_grid'),
    path('<int:pk>/', show_teachers_grid, name='show_teachers_grid'),
    path('recalculate/<int:pk>/', wage_recalculate, name='wage_recalculate'),
]
