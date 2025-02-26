# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/services/discount_service.py
# Author : Morice
# ---------------------------------------------------------------------------


from datetime import date
from django.utils.translation import gettext_lazy as _
from ..models import Discount

class DiscountService:
    @staticmethod
    def find_valid_discount_by_code(code):
        try:
            discount = Discount.objects.filter(code=code).first()

            if not discount:
                return None, _('Le code promo n\'existe pas')
            elif discount.end_date < date.today():
                return None, _('La promotion a expiré')
            else :
                return discount, _('ok')

        except Exception as e:
            print(f'Erreur discount_service find_valid_discound_by_code: {e}')
