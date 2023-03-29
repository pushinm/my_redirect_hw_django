from django.shortcuts import render
from django.views.generic.base import TemplateView
from teachers.models import Teacher
from subjects.models import Subject
from testimonials.models import Testimonial

from icecream import ic

# Create your views here.

def show_mainpage(request):
    template_ = 'mainpage.html'
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers,
    }
    return render(request=request, template_name=template_, context=context)


class MainpageView(TemplateView):
    template_name = 'mainpage.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = Teacher.objects.prefetch_related('subject').order_by('first_name').all()
        context['testimonials'] = Testimonial.objects.filter(active=True)

        return context