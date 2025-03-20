# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/prices.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models

class Price(models.Model):
    code = models.IntegerField(null=True,blank=True)
    service_name = models.CharField(max_length=50,null=False,blank=False)
    price_excl_tax = models.FloatField()
    price_excl_tax2 = models.FloatField(null=True,blank=True)
    price_excl_tax3 = models.FloatField(null=True,blank=True)
    distance_allowance = models.FloatField(null=True,blank=True)
    main_tax_info = models.CharField(max_length=60)
    main_tax_math = models.FloatField(null=True, blank=True)
    main_tax_name = models.CharField(max_length=100,null=True,blank=True)
    second_tax_info = models.CharField(max_length=60,null=True,blank=True)
    second_tax_math = models.FloatField(null=True, blank=True)
    second_tax_name = models.CharField(max_length=100,null=True,blank=True)
    is_created = models.DateTimeField(auto_created=True)
    is_obsolete = models.DateField(null=True,blank=True)
    is_active = models.BooleanField(default=False)

