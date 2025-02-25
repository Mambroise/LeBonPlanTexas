# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/services/discount_service.py
# Author : Morice
# ---------------------------------------------------------------------------


from datetime import datetime
from django.utils.translation import gettext_lazy as _
from ..models import Discount

class DiscountService:
    @staticmethod
    def find_valid_discount_by_code(code):
        try:
            discount = Discount.objects.get(code=code)
            if not discount:
                return False, _('Le code promo n\'existe pas')
            elif discount.end_date < datetime.now():
                return False, _('La promotion a expiré')
            else :
                return True, _('ok')

        except Exception as e:
            print(f'Erreur discount_service find_valid_discound_by_code: {e}')
