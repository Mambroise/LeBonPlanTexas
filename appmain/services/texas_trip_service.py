# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/services/texas_trip_service.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.db import IntegrityError

from ..models import Customer
from ..models.texas_trip import TexasTrip

class TexasTripService():
    @staticmethod
    def create_texas_trip(customer_id,texas_trip_data):
        try:
            # check if customer exists
            customer = Customer.objects.get(pk=customer_id)
            package = texas_trip_data['package']

            texas_trip = TexasTrip.objects.create(customer=customer,package=package)
            texas_trip.save()

            return texas_trip, True
        
        except Customer.DoesNotExist:
            print(f"No customer found with ID {customer_id}.")
            return None, False
        
        except (IntegrityError, ValueError) as e:
            print(f"Problem while creating TexasTrip : {e}")
            return None, False  
        
        except Exception as e:
            print(f"Problem occured : {e}")
            return None, False