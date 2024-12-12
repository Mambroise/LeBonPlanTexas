# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/trip.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from .customer import Customer

class Trip(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='trips')
    start_date = models.DateField(_('Date de début:'))
    end_date = models.DateField(_('Date de fin:'))
    cities = models.CharField(_('Villes:'),max_length=255,null=True)
    comment = models.TextField(_('Commentaire:'),max_length=500,null=True)
    vehiculed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"Trip for {self.customer} from {self.start_date} to {self.end_date}"
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and end_date < start_date:
            raise ValidationError({
                'Dates': _('Une erreur dans les dates est survenue.')
            })
        
        return cleaned_data