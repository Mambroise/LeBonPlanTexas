# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/services/interest_service.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.db import IntegrityError
from ..models import Category, Interest,Customer

class InterestService:
    @staticmethod
    def create_customer_interests(interest_list,customer_id):
        try:
            # check if customer exists
            customer = Customer.objects.get(pk=customer_id)
            
            # Retreive categories matching with id list
            categories = Category.objects.filter(id__in=interest_list)

            # create interest for each category retreived
            for category in categories:
                Interest.objects.create(
                    customer=customer,
                    category=category
                )

            return True
        except Customer.DoesNotExist:
            print(f"Client avec l'ID {customer_id} introuvable.")
            return False

        except (IntegrityError, ValueError) as e:
            print(f"Erreur lors de la création des catégories du client : {e}")
            return  False  
        
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")
            return  False