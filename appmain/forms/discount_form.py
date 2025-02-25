# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/forms/customer_form.py
# Author : Morice
# ---------------------------------------------------------------------------


from django import forms

from ..models import Discount

class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['code',]
        widgets = {
            'code': forms.TextInput(attrs={
                'class': 'discount-code',
            }),
        }