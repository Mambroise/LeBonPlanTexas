# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/index.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.shortcuts import render
from ..models import FileForImage,ImageDisplayTheme
from ..services import PriceService


def index(request):
    theme_displayed = ImageDisplayTheme.objects.get(is_active=True)
    files = FileForImage.objects.filter(is_active=True)
    auto, driver, plat = PriceService.get_active_prices()

    context = {
        'file_names':files,
        'theme_displayed':theme_displayed,
        'auto':auto,
    }

    return render(request, 'lebonplantexas/index.html',context)
