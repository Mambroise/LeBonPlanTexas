# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/index.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.shortcuts import render

def index(request):

    return render(request, 'lebonplantexas/index.html')
