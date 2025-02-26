# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/service/invoice_service.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.utils.timezone import now, timedelta
from django.db import IntegrityError
from django.utils.translation import gettext as _
from django.conf import settings

from ..models import Invoice,Price


class InvoiceService:
    @staticmethod
    def create_token(invoice: Invoice):
        try:
            invoice.generate_token()
            invoice.token_created_at = now()
            invoice.save()
            return True, invoice
        except (IntegrityError, ValueError) as e:
            print(f"Integrity or value problem while updating Invoice: {e}")
            return False, None
        except Exception as e:
            print(f"Unexpected problem while updating Invoice: {e}")
            return False, None

    @staticmethod
    def check_token_validity(token):
        if not token:
            print("Token is missing.")
            return None, False, _('Le token est introuvable.')

        try:
            # Récupération de la facture associée au token
            invoice = Invoice.objects.filter(token=token, is_paid=False).first()

            if not invoice:
                invoice = InvoiceService.invoice_is_paid(token)
                if invoice:
                    return invoice, False, None
                else:
                    return None, False, _('La facture est introuvable')

            # Vérification de l'expiration
            token_validity_period = timedelta(seconds=settings.PAYMENT_TOKEN_VALIDITY)
            if now() > invoice.token_created_at + token_validity_period:
                return invoice, False, _("Validité du token expirée.")

            return invoice, True, None
        except Exception as e:
            print(f"Unexpected problem while checking token: {e}")
            return None, False, _("Une erreur s'est produite lors de la vérification du token: %s." % str({e}))

    @staticmethod
    def create_invoice(customer, trips, texas_trip,discount):
        if texas_trip.package == '1':
            total = 0
            for trip in trips:
                nbr_days = (trip.end_date - trip.start_date).days
                total += nbr_days
            price = Price.objects.get(service_name='autonome')
            invoice = Invoice(customer=customer,
                              texas_trip=texas_trip,
                              mobile_service=True,
                              nbr_days_mobile=total,
                              discount=discount,
                              mobile_price_excl_tax=price.price_excl_tax)
            invoice.save()
            # create invoice token
            success, invoice = InvoiceService().create_token(invoice)
            if success:
                return True,invoice
        else:
            return False,None
            


    @staticmethod
    def invoice_is_paid(token):
        invoice = Invoice.objects.get(token=token, is_paid=True)
        
        if invoice:
            return invoice
        else:
            return None
        
        