# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/service.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.shortcuts import render

from ..services import PriceService

def service_view(request):
    # preparing package availability context for html columns
    auto, driver, plat = PriceService.get_active_prices()

    context = {
        'auto':auto,
        'driver':driver,
        'plat':plat,
    }
    return render(request,'lebonplantexas/services.html',context)