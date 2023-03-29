from django.contrib import admin
from wages.models import Wage


# Register your models here.

class WageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'teacher', 'salary', 'tax', 'deductions', 'alimony', 'net',)
    list_display_links = ('pk',)
    list_editable = ('teacher', 'salary', 'tax', 'deductions', 'alimony',)
    search_fields = ('teacher', )
    readonly_fields = ('net',)
    
admin.site.register(Wage, WageAdmin)    
