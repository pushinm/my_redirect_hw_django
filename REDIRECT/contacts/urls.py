from django.urls import path
from .views import contact_page, contact_form_save

app_name = 'contacts'

urlpatterns = [
    path('', contact_page, name='contact_page'),
    path('form_save/', contact_form_save, name='contact_form_save')
]
