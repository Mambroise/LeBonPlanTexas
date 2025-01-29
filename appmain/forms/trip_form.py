# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/forms/customer_form.py
# Author : Morice
# ---------------------------------------------------------------------------


from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils.timezone import now

from appmain.models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['start_date','end_date','cities','comment','nbr_days_driver']
    
        widgets = {
            "start_date": forms.DateInput(attrs={
                "type": "date", 
                "style": ("font-size: 1.3rem;"
                          "padding : 10px;"
                          "border-radius : 10px;"
                          ),
            }),
            "end_date": forms.DateInput(attrs={
                "type": "date", 
                "style": ("font-size: 1.3rem;"
                          "padding : 10px;"
                          "border-radius : 10px;"
                          ),
            }),
            "nbr_days_driver": forms.NumberInput(attrs={
                "class": "custom-integer_input",
                "style": ("width : 5rem;"
                          ),
            }),
            "comment": forms.Textarea(attrs={
                "class": "custom-placeholder",
                "style": ("width : 100%;"
                          "margin : auto;"
                          "height : 100%;"   
                          ),
                "placeholder": _("Commentaire :information utile, adresse complète de l'hotel..."),
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].required = False
        self.fields['nbr_days_driver'].required = False

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        # Vérification que start_date n'est pas dans le passé
        if start_date and start_date < now().date():
            raise ValidationError({'start_date': _("La date de début ne peut pas être antérieure à aujourd'hui.")})

        # Vérification que end_date est après start_date (déjà implémentée mais renforcée ici)
        if start_date and end_date and end_date < start_date:
            raise ValidationError({'end_date': _("La date de fin doit être postérieure à la date de début.")})

        return cleaned_data