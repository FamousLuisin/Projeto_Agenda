from django.shortcuts import render
from contact import models

# Create your views here.
def index(request):
    contacts = models.Contact.objects.all()
    context = {
        'contacts': contacts,
    }


    return render(
        request,
        'contact/index.html',
        context
    )