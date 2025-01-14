# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/service.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.shortcuts import render

def service_view(request):

    return render(request,'lebonplantexas/services.html')