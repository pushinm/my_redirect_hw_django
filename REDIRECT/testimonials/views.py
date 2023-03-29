from django.shortcuts import render
from  django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView , RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from icecream import ic
from .models import Testimonial
from .forms import TestimonialForm

# Create your views here.

class TestimonialListViews(LoginRequiredMixin, ListView):
    model = Testimonial
    template_name = 'testimonials/testimonials_list.html'
    context_object_name = 'testimonials'

class TestimonquialCreateView(CreateView):
    model = Testimonial
    template_name = 'testimonials/testimonial_form.html'
    success_url = reverse_lazy('mainpage:mainpage')
    form_class = TestimonialForm

class TestimonialUpdateView(LoginRequiredMixin, UpdateView):
    model = Testimonial
    template_name = 'testimonials/testimonial_form.html'
    success_url = reverse_lazy('testimonials:testimonials_list')
    form_class = TestimonialForm


class TestimonialDeleteView(LoginRequiredMixin, DeleteView):
    model = Testimonial
    template_name = 'testimonials/testimonial_confirm_delete.html'
    success_url = reverse_lazy('mainpage:mainpage')


class My_redirect_view(RedirectView):
    permanent = False
    url = '/testimonials/'
