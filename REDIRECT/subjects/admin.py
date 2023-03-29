from django.contrib import admin
from .models import Subject

from icecream import ic
# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('pk',)
    search_fields = ('pk', 'name')
    list_editable = ('name',)
    pass



admin.site.register(Subject, SubjectAdmin)

# admin.site.register(Classroom, ClassroomAdmin)

