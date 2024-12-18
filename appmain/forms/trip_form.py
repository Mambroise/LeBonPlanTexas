# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/forms/customer_form.py
# Author : Morice
# ---------------------------------------------------------------------------


from django import forms

from appmain.models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['start_date','end_date','cities','comment','vehiculed']
    
        widgets = {
            "start_date" : forms.DateInput(attrs={"type" : "date"}),
            "end_date" : forms.DateInput(attrs={"type" : "date"})
        }
