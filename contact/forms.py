from collections.abc import Mapping
from typing import Any
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from . import models
from django import forms

class ContactForm(forms.ModelForm):
    # Forma 1 de trabalhar com um campo de input
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class':'classe-a',
    #             'placeholder':'Primeiro nome',
    #         }
    #     ),
    #     label= 'Primeiro nome',
    #     help_text='texto de ajuda',
    # )
    
    # Forma 2 de trabalhar com um campo de input
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)  
        # self.fields['first_name'].widget.attrs.update({
        #     'class':'classe-c',
        #     'placeholder':'Primeiro nome'
        # })
    
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture')

        # Forma 3 de trabalhar com um campo de input
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class':'classe-a classe-b',
        #             'placeholder': 'Escreva aqui'
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error(
            'last_name', ValidationError('Primeiro nome não pode ser igual ao segundo', code='invalid')
            )
        

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
            self.add_error(
            'first_name', ValidationError('Mensagem de erro do clean_first_name', code='invalid')
        )
            
        return first_name