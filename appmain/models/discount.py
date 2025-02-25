# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/discount.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models

from .service_package import PackageChoice

class Discount(models.Model):
    code = models.CharField(max_length=10,null=False,blank=True)
    target = models.IntegerField(choices=PackageChoice.choices,default=PackageChoice.AUTONOMOUS)
    rate = models.CharField(max_length=6,null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return f'discount: {self.code}, {self.rate}'