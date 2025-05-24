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
from django.db.models import Sum


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
    def create_invoice(customer, texas_trip, discount):
        
        mobile_price = 0.0
        driver_price = None
        platinum_price = None
        driver_service_status = False
        platinum_service_status = False
        nbr_days_driver_total = 0
        nbr_days_platinum_total = 0

        try:
            if texas_trip.package == '1':
                price = Price.objects.get(code=100)
                mobile_price = price.price_excl_tax
            elif texas_trip.package == '2':
                price = Price.objects.get(code=200)
                driver_price = price.price_excl_tax
                driver_service_status = True

                nbr_days_driver_total = texas_trip.whole_trips.aggregate(
                total_days=Sum('nbr_days_driver')
                )['total_days'] or 0

            elif texas_trip.package == '3':
                price = Price.objects.get(code=300)
                platinum_price = price.price_excl_tax
                platinum_service_status = True

                nbr_days_platinum_total = texas_trip.whole_trips.aggregate(
                total_days=Sum('nbr_days_driver')
                )['total_days'] or 0

            else:
                return False, None

            invoice = Invoice(
                customer=customer,
                texas_trip=texas_trip,
                mobile_service=True,
                driver_service=driver_service_status,
                platinum_service=platinum_service_status,
                discount=discount,
                mobile_price_excl_tax=mobile_price,
                driver_price_excl_tax=driver_price,
                platinum_price_excl_tax=platinum_price,
                nbr_days_driver=nbr_days_driver_total,
                nbr_days_platinum=nbr_days_platinum_total
            )
            invoice.save()

            success, invoice = InvoiceService().create_token(invoice)
            if success:
                return True, invoice

        except Exception as e:
            print(f"error in InvoiceService.create_invoice: {e}")
            return False, None

            
    @staticmethod
    def set_invoice_number(customer_id,texas_trip_id, invoice_id):
        today_str = now().strftime('%Y%m%d')
        return f'{invoice_id}{customer_id}{today_str}'


    @staticmethod
    def invoice_is_paid(token):
        invoice = Invoice.objects.get(token=token, is_paid=True)
        
        if invoice:
            return invoice
        else:
            return None
        
        