from django.contrib import admin
from .models import Teacher


# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'birth_day', 'email', 'phone',)
    list_display_links = ('pk',)
    search_fields = ('first_name', 'last_name', 'birth_day', 'email', 'phone')
    list_editable = ('first_name', 'last_name', 'email', 'phone',)


admin.site.register(Teacher, TeacherAdmin)
