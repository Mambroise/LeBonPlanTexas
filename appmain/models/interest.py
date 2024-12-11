# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/trip.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models
from django.utils.translation import gettext_lazy as _

from appmain.models import Customer,Category

class Interest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='interests')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='interested_customers')

    class Meta:
        unique_together = ('customer', 'category')

    def __str__(self):
        return f"{self.customer} is interested in {self.category}"