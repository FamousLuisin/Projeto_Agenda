from django.shortcuts import render, get_object_or_404, redirect
from contact import models
from django.http import Http404
from django.db.models import Q


# Create your views here.
def index(request):
    contacts = models.Contact.objects.filter(show=True).order_by('-id')[0:10]

    context = {
        'contacts': contacts,
        'site_title': 'contatos - ',
    }


    return render(
        request,
        'contact/index.html',
        context
    )


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    # Esse Q, permite usar o | para ser usado como or
    contacts = models.Contact.objects.filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')

    context = {
        'contacts': contacts,
        'site_title': 'contatos - ',
        'search_value': search_value,
    }


    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, contact_id):
    # single_contact = models.Contact.objects.filter(pk=contact_id).first()
    # if single_contact is None:
    #     raise Http404()

    single_contact = get_object_or_404(models.Contact, pk=contact_id, show=True)
    contact_name = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': contact_name,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )