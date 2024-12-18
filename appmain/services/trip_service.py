# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/services/customer_service.py
# Author : Morice
# ---------------------------------------------------------------------------

# appmain/services/trip_service.py
from appmain.models import Trip
from django.db import IntegrityError

class TripService:
    @staticmethod
    def create_trip(data, customer_id):
        try:
            # Création d'un nouvel objet Trip
            trip = Trip(
                customer_id=customer_id,  
                start_date=data.get('start_date'),  
                end_date=data.get('end_date'),  
                cities=data.get('cities'),  
                comment=data.get('comment'),  
                vehiculed=data.get('vehiculed', False),  
            )
            trip.save()  # Enregistre l'objet dans la base de données

            return True  # Indique que la création du voyage a réussi
        except IntegrityError as e:
            # Gère les erreurs d'intégrité, par exemple si des contraintes sont violées
            print(f"Erreur d'intégrité : {e}")
            return False
        except Exception as e:
            # Gère toutes les autres erreurs
            print(f"Erreur lors de la création du voyage : {e}")
            return False
