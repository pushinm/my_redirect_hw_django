from django.contrib import admin
from .models import Classboard


# Register your models here.


class ClassboardAdmin(admin.ModelAdmin):
    list_display = ('pk', 'class_day', 'class_pair', 'subject_name', 'group', 'show_teachers')
    list_display_links = ('pk',)
    search_fields = ('pk', 'subject_name', 'class_pair', 'subject_name', 'group',)
    list_editable = ('subject_name', 'class_pair', 'subject_name', 'group',)

    def show_teachers(self, obj):
        return "\n".join([item.first_name + ' ' + item.last_name + ',' for item in obj.teacher.all()])
    

admin.site.register(Classboard, ClassboardAdmin)
