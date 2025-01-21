# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/services/customer_service.py
# Author : Morice
# ---------------------------------------------------------------------------


from ..models import CompanyInfo

class CompanyService:
    @staticmethod
    def get_company_info():
       return CompanyInfo.objects.all().first()
