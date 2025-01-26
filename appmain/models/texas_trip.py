# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/texas_trip.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models

from .trip import Customer
from .service_package import PackageChoice

class TexasTrip(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='one_trip')
    package = models.IntegerField(choices=PackageChoice.choices,default=PackageChoice.AUTONOMOUS)
    created_at = models.DateTimeField(auto_now=True)
