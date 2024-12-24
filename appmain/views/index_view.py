# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/customer.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def index(request):

    return render(request, 'lebonplantexas/index.html')
