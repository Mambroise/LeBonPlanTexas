# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/category.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models
class CompanyInfo(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    EIN = models.CharField(max_length=20,null=True,blank=True)
    SIREN = models.CharField(max_length=20,null=True,blank=True)
    legal_structure = models.CharField(max_length=30,null=True, blank=True)
    address = models.CharField(max_length=155)
    tax_info= models.CharField(max_length=6)
    tax_math = models.FloatField(null=True, blank=True)
    email = models.CharField(max_length=150,unique=True)
    phone = models.CharField(max_length=15, blank=True,null=True)
    instagram = models.CharField(max_length=50)
    is_in_texas = models.BooleanField(default=False)