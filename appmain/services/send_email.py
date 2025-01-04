# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/service/send_email.py
# Author : Morice
# ---------------------------------------------------------------------------


import secrets
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from decouple import config

from ..models import Customer,Invoice,Category

def send_payment_link(customer: Customer,invoice:Invoice):
    try:
        object_content = _('LeBonPlanTexas : Voici le devis de votre voyage!')
        company_name = _('LebonPlanTEXAS')
        payment_url_with_token = 'http://127.0.0.1:8000/payment/?token=' + invoice.token


        email_body = { 
            'company_name': company_name,
            'trip_invoice' : invoice,
            'token_url' : payment_url_with_token
        }

        # Render the email template with context data
        subject = object_content
        from_email = config('EMAIL_HOST_USER')
        to_email = customer.email
        text_content = 'Your email client does not support HTML content'

        html_payment_link_content = render_to_string('email/payment_link_email.html', email_body)
        
        # Create the email message
        email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        email.attach_alternative(html_payment_link_content, 'text/html')

        # Send the email
        email.send()
        return True
        
    except:
        return False

    

def success_registration_email(customer, trips, interests):
    categories = dict(Category.objects.values_list('id', 'name'))
    customer_interests = [categories[interest] for interest in interests if interest in categories]
    company_email = config('EMAIL_HOST_USER')
    
    object_content =_('LeBonPlanTEXAS : On se parle bientôt!!')
    company_name = _('LebonPlanTEXAS')

    email_body = {
        'company_name' : company_name,
        'customer' : customer,
        'trips' : trips,
        'interests' : customer_interests,
        'company_email' : company_email
    }

    # Render the email template with context data
    subject = object_content
    from_email = company_email
    to_email = customer.email
    text_content = 'Your email client does not support HTML content'

    html_payment_link_content = render_to_string('email/success_registration_email.html', email_body)

    # Create the email message
    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_payment_link_content, 'text/html')

    # Send the email
    email.send()