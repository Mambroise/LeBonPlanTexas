# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/trip.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models
from django.utils.translation import gettext_lazy as _

from .customer import Customer

class Trip(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='trips')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Trip for {self.customer} from {self.start_date} to {self.end_date}"