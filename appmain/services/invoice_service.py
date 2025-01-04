# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/service/invoice_service.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import IntegrityError

from ..models import Invoice
from datetime import datetime


class InvoiceService:
    @staticmethod
    def create_token(invoice : Invoice):
        try:
            invoice.generate_token()
            invoice.token_created_at = datetime.now()
            invoice.save()

            return True,invoice
        
        except (IntegrityError, ValueError) as e:
            print(f"Problem while updating Invoice : {e}")

            return False,None