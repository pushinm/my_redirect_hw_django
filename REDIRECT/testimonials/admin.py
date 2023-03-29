from django.contrib import admin
from .models import Testimonial
# Register your models here.


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('title', 'testimonial', 'create_at', 'update_at', 'active')
    list_editable = ('active',)
    search_fields = ('title', 'testimonial', 'create_at', 'update_at')
    list_filter = ('title', 'testimonial', 'create_at', 'update_at')

admin.site.register(Testimonial, TestimonialAdmin)