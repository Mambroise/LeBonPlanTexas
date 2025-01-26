# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/service_package.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models
from django.utils.translation import gettext_lazy as _

class PackageChoice(models.IntegerChoices):
    AUTONOMOUS = 1,_('autonome')
    PRIVATE_DRIVER = 2,_('chauffeur privée')
    PLATINUM = 3,_('platinum')