# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/customer.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Customer(models.Model):

    first_name = models.CharField(_('Prénom:'), max_length=100)
    last_name = models.CharField(_('Nom:'), max_length=150)
    email = models.CharField(_('Email:'), max_length=150)
    phone = models.IntegerField(_('Portable:'), blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"