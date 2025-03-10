# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/services/customer_service.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import IntegrityError
from appmain.models import Customer

class CustomerService:
    #  Method to create a customer
    @staticmethod
    def create_customer(data):
        """
        Creates a customer based on the provided data.

        :param data: Dictionary containing customer data (form.cleaned_data).
        :return: Tuple (customer_id, success), where success is a boolean indicating whether the operation was successful.
        """

        try:
            # Checking data
            required_fields = ['first_name', 'last_name', 'email', 'phone']
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Field {field} is missing data.")

            # Creating customer instance
            customer = Customer.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                phone=data['phone'],
                country=data['country']
            )
            customer.full_clean() 
            customer.save()

            return customer, True 

        except (IntegrityError, ValueError) as e:
            print(f"A problem occured while creating a customer : {e}")
            return None, False  
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")
            return None, False

    # method to delete customer
    @staticmethod
    def delete_customer(customer_id):
        try:
            customer = Customer.objects.get(pk=customer_id)
            customer.delete()
            print('Customer successfully deleted')
        except Exception as e:
            print(f'Customer not deleted: {e}')

    
    @staticmethod
    def customer_is_mailed(customer : Customer):
        try:
            customer.is_mailed = True
            customer.save()
            print(f'is_mailed successfully updated ')
        except Exception as e:
            print(f'is_mailed update unsuccessful: {e}')

    @staticmethod
    def find_by_id(customer_id):
        try:
            customer = Customer.objects.get(pk=customer_id)
            return customer
        except:
            print('customer not found in customer_service find_by_id')
            return None