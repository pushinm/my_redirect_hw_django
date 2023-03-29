from django.contrib import admin
from .models import ContactPage, ContactPageForm
# Register your models here.

class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('description', 'office', 'phone')

class ContactPageFormAdmin(admin.ModelAdmin):
    list_display = ('subject', 'message')

admin.site.register(ContactPage, ContactPageAdmin)
admin.site.register(ContactPageForm, ContactPageFormAdmin)