# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/service.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.shortcuts import render

from ..models import Price

def service_view(request):
    # preparing package availability context for html columns
    prices = Price.objects.all()
    if prices:
        auto = None
        driver = None
        plat = None
        for price in prices:
            if price.service_name == 'autonome' and price.is_active == True:
                auto = price
            elif price.service_name == 'chauffeur privé' and price.is_active == True:
                driver = price
            elif price.service_name == 'platinium' and price.is_active == True:
                plat = price

        context = {
            'auto':auto,
            'driver':driver,
            'plat':plat,
        }
    return render(request,'lebonplantexas/services.html',context)