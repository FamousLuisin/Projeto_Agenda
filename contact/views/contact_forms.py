from django.shortcuts import render, redirect
from contact import forms

def create(request): 
    if request.method == 'POST':
        form = forms.ContactForm(data=request.POST)
        
        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:create')
        
        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
            'form': forms.ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )
