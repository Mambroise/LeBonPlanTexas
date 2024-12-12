# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/customer.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.shortcuts import render
from django.http import HttpRequest

from ..forms.customer_form import CustomerForm
from ..forms.trip_form import TripForm
from ..models import Category

# Create your views here.
def register_view(request: HttpRequest):
    if request.method == 'POST':
        pass
    customer_form = CustomerForm()
    trip_form = TripForm()
    categories = Category.objects.all()
    context = {'customer_form': customer_form,
                'trip_form': trip_form,
                'categories': categories}
    return render(request,'lebonplantexas/landing.html', context)