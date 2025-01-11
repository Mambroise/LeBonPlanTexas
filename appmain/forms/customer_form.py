# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/forms/customer_form.py
# Author : Morice
# ---------------------------------------------------------------------------


from django import forms
from django_countries.widgets import CountrySelectWidget

from appmain.models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name','last_name','email','phone','country']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'country': CountrySelectWidget(attrs={
                'class': 'form-control',
                'required': True, 
            }),
        }
