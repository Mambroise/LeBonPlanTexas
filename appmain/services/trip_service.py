# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/services/trip_service.py
# Author : Morice
# ---------------------------------------------------------------------------


from appmain.models import Trip
from django.db import IntegrityError

class TripService:
    @staticmethod
    def create_trip(data, customer_id,texas_trip_id):
        try:
            # Creating Trip object
            trip = Trip(
                customer_id=customer_id,
                texas_trip_id = texas_trip_id,  
                start_date=data.get('start_date'),  
                end_date=data.get('end_date'),  
                cities=data.get('cities'),  
                comment=data.get('comment'),  
                nbr_days_driver=data.get('nbr_days_driver', 0),  
            )
            trip.save()  

            return True  
        except IntegrityError as e:
            # Gère les erreurs d'intégrité, par exemple si des contraintes sont violées
            print(f"Erreur d'intégrité dans trip_service.py: {e}")
            return False
        except Exception as e:
            # Gère toutes les autres erreurs
            print(f"Erreur lors de la création du voyage dans trip_service.py : {e}")
            return False
