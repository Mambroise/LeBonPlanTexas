# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/service/price_service.py
# Author : Morice
# ---------------------------------------------------------------------------

from ..models import Price

class PriceService:
    @staticmethod
    def get_active_prices():
        prices = Price.objects.all()
        if prices:
            auto = None
            driver = None
            plat = None

            for price in prices:
                if (price.service_name == 'autonome' or price.service_name == 'autonomous' or price.service_name == 'autonomo') and price.is_active == True:
                    auto = price    
                elif (price.service_name == 'chauffeur privé' or price.service_name == 'personal driver' or price.service_name == 'chofer privado') and price.is_active == True:
                    driver = price
                elif (price.service_name == 'platinium' or price.service_name == 'platinum' or price.service_name == 'platino') and price.is_active == True:
                    plat = price

        return auto, driver, plat