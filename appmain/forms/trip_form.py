# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/forms/customer_form.py
# Author : Morice
# ---------------------------------------------------------------------------


from django import forms
from django.utils.translation import gettext_lazy as _

from appmain.models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['start_date','end_date','cities','comment','vehiculed']
    
        widgets = {
            "start_date": forms.DateInput(attrs={
                "type": "date", 
                "style": "font-size: 1rem;",
            }),
            "end_date": forms.DateInput(attrs={
                "type": "date", 
                "style": "font-size: 1rem;",
            }),
            "comment": forms.Textarea(attrs={
                "style": ("font-size: 1.25rem;"
                          "width : 100%;"  
                          ),
                "placeholder": _("Information utile, adresse complète de l'hotel..."),
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].required = False