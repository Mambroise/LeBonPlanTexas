# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/trip.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from ..models import Customer
from appmain.models.texas_trip import TexasTrip

class Trip(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='trips')
    texas_trip = models.ForeignKey(
        TexasTrip, 
        on_delete=models.CASCADE, 
        related_name='whole_trips',
        null=True,  
        blank=True
    )
    start_date = models.DateField(_('Début:'))
    end_date = models.DateField(_('Fin:'))
    cities = models.CharField(_('Villes'),max_length=255,null=True)
    comment = models.TextField(_('Commentaire:'),max_length=500,null=True)
    nbr_days_driver = models.IntegerField(_("Nombre de jour de service"), max_length=3,null=False, blank=False,default=0)
    timestamp = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"Trip for {self.customer} from {self.start_date} to {self.end_date}"
    
    def clean(self):
        super().clean()  # Appelle la méthode clean parente
        if self.start_date and self.end_date and self.end_date < self.start_date:
            raise ValidationError({
                'end_date': _('La date de fin doit être postérieure à la date de début.')
            })
