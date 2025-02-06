# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/payment.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.shortcuts import render
from ..services.invoice_service import InvoiceService

def payment_view(request):
    token = request.GET.get('token')

    # Vérification du token
    invoice, success, message = InvoiceService.check_token_validity(token)
    
    # case : Invoice already paid
    if invoice and not success:
        context = {'trip_invoice' : invoice,
                   'customer_email' : invoice.customer.email,
                   'amount_paid' : invoice.total}
        
        return render(request, 'lebonplantexas/checkout_success.html', context )
   
    # case : 
    if not success and not invoice:
         print('message:',message)
         return render(request, "error.html", {"message": message})

    # cas: everything ok, go to accept terms of use modal
    return render(request, 'lebonplantexas/accept_terms_of_sale.html',{'invoice':invoice})
