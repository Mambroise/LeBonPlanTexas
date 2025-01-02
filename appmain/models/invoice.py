# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/invoice.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models
from django.utils.translation import gettext as _
from ..models import Customer
from appmain.models.texas_trip import TexasTrip

class Invoice(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('1', _('Pending')),
        ('2', _('Paid')),
        ('3', _('Rejected'))
    ] 

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    texas_trip = models.OneToOneField(TexasTrip, on_delete=models.CASCADE, related_name='trip_invoice')
    # classic service part
    mobile_service = models.BooleanField(default=False)
    nbr_days_mobile = models.IntegerField(null=True,blank=True)
    price_mobile = models.FloatField(null=True,blank=True)
    # driver service part
    driver_service = models.BooleanField(default=False)
    nbr_days_driver = models.IntegerField(null=True,blank=True)
    price_driver = models.FloatField(null=True,blank=True)
    # platinum service part
    platinum_service = models.BooleanField(default=False)
    nbr_days_platinum = models.IntegerField(null=True,blank=True)
    price_platinum = models.FloatField(null=True,blank=True)

    total = models.FloatField(null=True,blank=True)
    payment_type = models.CharField(max_length=20,default="Credit card")
    status = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES, default="1")
