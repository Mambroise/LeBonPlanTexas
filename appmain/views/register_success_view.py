# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/register_success_view.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.shortcuts import render
from ..services.customer_service import CustomerService

def register_success(request,customer_id):
    customer = CustomerService.find_by_id(customer_id)
    return render(request,'lebonplantexas/register_success.html',{'customer':customer})