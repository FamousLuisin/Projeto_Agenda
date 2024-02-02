from django.shortcuts import render, redirect, get_object_or_404
from contact import forms
from django.urls import reverse
from contact import models

def create(request):
    form_action = reverse('contact:create') 
    if request.method == 'POST':
        form = forms.ContactForm(data=request.POST)
        
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
        
        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
            'form': forms.ContactForm(),
            'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )


def update(request, contact_id):
    contact = get_object_or_404(models.Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,)) 

    if request.method == 'POST':
        form = forms.ContactForm(data=request.POST, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
        
        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
            'form': forms.ContactForm(instance=contact),
            'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )

def delete(request, contact_id):
    contact = get_object_or_404(models.Contact, pk=contact_id, show=True)

    confirmation = request.POST.get('confirmation', 'no')
    
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    
    

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation
        }
    )