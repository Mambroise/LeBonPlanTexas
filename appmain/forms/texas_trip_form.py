# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/forms/texas_trip_form.py
# Author : Morice
# ---------------------------------------------------------------------------


from django import forms

from ..models import TexasTrip
from ..models.service_package import PackageChoice

class TexasTripForm(forms.ModelForm):
    package = forms.ChoiceField(choices=PackageChoice.choices,
                                widget=forms.RadioSelect(attrs={'class': 'd-none'}),
                                required=True)
    class Meta:
        model = TexasTrip
        fields = ('package',)
