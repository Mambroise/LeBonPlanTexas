# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/invoice.py
# Author : Morice
# ---------------------------------------------------------------------------


import secrets
from django.db import models
from django.utils.translation import gettext as _
from django.utils.timezone import now

from ..models import Customer,Discount
from appmain.models.texas_trip import TexasTrip

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    texas_trip = models.OneToOneField(TexasTrip, on_delete=models.CASCADE, related_name='trip_invoice')
    invoice_number = models.CharField(max_length=100,null=True,blank=True, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    # classic service part
    mobile_service = models.BooleanField(default=False)
    mobile_price_excl_tax = models.FloatField(null=True,blank=True)
    # driver service part
    driver_service = models.BooleanField(default=False)
    nbr_days_driver = models.IntegerField(null=True,blank=True)
    driver_price_excl_tax = models.FloatField(null=True,blank=True)
    # platinum service part
    platinum_service = models.BooleanField(default=False)
    nbr_days_platinum = models.IntegerField(null=True,blank=True)
    platinum_price_excl_tax = models.FloatField(null=True,blank=True)
    # token part
    token = models.CharField(max_length=100,null=True,blank=True)
    token_created_at = models.DateTimeField(null=True,blank=True)
    terms_of_sale_accepted = models.BooleanField(default=False)
    terms_of_sale_accepted_date = models.DateTimeField(null=True,blank=True)

    tax_rate = models.FloatField(null=True,blank=True)
    tax_amount = models.FloatField(null=True,blank=True)
    total_excl_tax = models.FloatField(null=True,blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.DO_NOTHING, related_name='all_invoices_with_discounts',null=True,blank=True)
    total = models.FloatField(null=True,blank=True)
    total_incl_discount = models.FloatField(null=True,blank=True)
    payment_type = models.CharField(max_length=20,default="Credit card")
    is_paid = models.BooleanField(default=False)
    is_paid_date = models.DateTimeField(null=True,blank=True)
    stripe_session_id = models.CharField(max_length=255,null=True,blank=True)


    def generate_token(self):
        self.token = secrets.token_hex(32)

