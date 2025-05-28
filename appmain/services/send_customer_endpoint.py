# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/api/send_customer_endpoint.py
# Author : Morice
# ---------------------------------------------------------------------------


import requests
from django.conf import settings
from appmain.serializers import CustomerSerializer

def send_customer_to_external_api(invoice):
    customer = invoice.customer
    if not customer:
        return {"success": False, "message": "No customer found"}

    serializer = CustomerSerializer(customer)
    customer_data = serializer.data

    try:
        response = requests.post(
            settings.EXTERNAL_CUSTOMER_API_URL,
            json=customer_data,
            timeout=5
        )
        if response.status_code in [200, 201]:
            return {"success": True, "message": "Customer sent successfully"}
        else:
            return {
                "success": False,
                "message": f"Erreur API distante : {response.status_code} - {response.text}"
            }
    except requests.exceptions.RequestException as e:
        return {"success": False, "message": str(e)}
