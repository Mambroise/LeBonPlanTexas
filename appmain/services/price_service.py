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
                if (price.service_name == 'autonome' or price.service_name == 'autonomous') and price.is_active == True:
                    print('ok auto')
                    auto = price    
                    print(auto)
                elif (price.service_name == 'chauffeur privé' or price.service_name == 'personal driver') and price.is_active == True:
                    print('ok driver')
                    driver = price
                    print(driver)
                elif (price.service_name == 'platinium' or price.service_name == 'platinum') and price.is_active == True:
                    print('ok plat')
                    plat = price
                    print(plat)
        print(auto)
        print(driver)
        print(plat)
        return auto, driver, plat