# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/privacy.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from ..services.company_service import CompanyService


def privacy(request):
    company_info = CompanyService.get_company_info()
    return render(request, 'lebonplantexas/privacy_policy.html', {'company_info':company_info})