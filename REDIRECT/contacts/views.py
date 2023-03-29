from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_http_methods
from django.urls import reverse

from .forms import ContactFormDB
from .models import ContactPage, ContactPageForm

from icecream import ic

# Create your views here.

def contact_page(request):
    template_ = 'contact_page.html'
    contact_page = get_object_or_404(ContactPage, pk=1)
    # contact_form = ContactForm();
    contact_form_db = ContactFormDB()

    context = {
        'contact_page': contact_page,
        # 'contact_form': contact_form,
        'contact_form_db': contact_form_db,
    }

    return render(request=request, template_name=template_, context=context)


@require_http_methods(["GET", "POST"])
def contact_form_save(request):

    if request.method in 'POST':
        form = ContactFormDB(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse('contacts:contact_page'))
