# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/service/send_email.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.conf import settings
import os
from email.mime.image import MIMEImage

from ..models import Customer,Invoice,Category
from ..services.company_service import CompanyService

def send_payment_link(customer: Customer,invoice:Invoice):
    try:
        domain = settings.DOMAIN
        object_content = _('LeBonPlanTexas : DEVIS pour votre voyage!')
        payment_url_with_token = f'{domain}/payment/?token=' + invoice.token
        company_info = CompanyService.get_company_info()

        email_body = { 
            'company_info': company_info,
            'trip_invoice' : invoice,
            'token_url' : payment_url_with_token
        }

        # Render the email template with context data
        subject = object_content
        from_email = company_info.email
        to_email = customer.email
        text_content = 'Your email client does not support HTML content'

        html_payment_link_content = render_to_string('email/payment_link_email.html', email_body)
        
        # Create the email message
        email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        email.attach_alternative(html_payment_link_content, 'text/html')

        # attach picture to email
        email = attach_pic_to_email(email)

        # Send the email
        email.send()
        return True
        
    except Exception as e:
        print('send_payment_link email error:', {e})
        return False

def success_registration_email(customer, texas_trip, trips, interests):
    try:
        categories = dict(Category.objects.values_list('id', 'name'))
        company_info = CompanyService.get_company_info()
        customer_interests = [categories[interest] for interest in interests if interest in categories]
        
        
        object_content =_('LeBonPlanTEXAS : On se parle bientôt!!')

        email_body = {
            'company_name' : company_info.name,
            'customer' : customer,
            'texas_trip': texas_trip,
            'trips' : trips,
            'interests' : customer_interests,
            'company_email' : company_info.email,
        }

        # Render the email template with context data
        subject = object_content
        from_email = company_info.email
        to_email = customer.email
        bcc_email = [company_info.email] 
        text_content = 'Your email client does not support HTML content'

        html_email_content = render_to_string('email/success_registration_email.html', email_body)

        # Create the email message
        email = EmailMultiAlternatives(subject, text_content, from_email, [to_email], bcc=bcc_email)
        email.attach_alternative(html_email_content, 'text/html')

        # attach picture to email
        email = attach_pic_to_email(email)

        # Send the email
        email.send()
    except Exception as e:
        print(f'erreur dans l\'envoi du mail de registration: {e}')


def send_checkout_success_email(invoice):
    try:
        company_info = CompanyService.get_company_info()
        # Objet de l'email
        subject = _('LeBonPlanTexas : Votre paiement est confirmé!')
        from_email = company_info.email 
        to_email = invoice.customer.email
        bcc_email = [company_info.email ] 
        text_content = 'Your email client does not support HTML content'
        
        # Contenu du template HTML
        email_body = {
            'company_info': company_info,
            'trip_invoice': invoice,
        }
        html_payment_link_content = render_to_string('email/checkout_success_email.html', email_body)

        # Contenu alternatif pour les clients email sans HTML
        text_content = _('Your email client does not support HTML content')

        # create l'email
        email = EmailMultiAlternatives(subject, text_content, from_email, [to_email],bcc=bcc_email)
        email.attach_alternative(html_payment_link_content, 'text/html')

        # attach picture to email
        email = attach_pic_to_email(email)
                
        email.send()
        return True

    except Exception as e:
        print('Erreur lors de l\'envoi de l\'email :', e)
        return False
    
def attach_pic_to_email(email):
            # Attachez les images nécessaires avec Content-ID
    image_paths = {
            'fort_worth': 'static/images/fort_worth_stockyards_coliseum.jpg',
        }

    for cid, img_path in image_paths.items():
        absolute_path = os.path.join(settings.BASE_DIR, img_path)
        with open(absolute_path, 'rb') as img:
            mime_img = MIMEImage(img.read())
            mime_img.add_header('Content-ID', f'<{cid}>')
            mime_img.add_header('Content-Disposition', 'inline')
            email.attach(mime_img)
    return email


def estimate_validation(customer, texas_trip, trips, interests, invoice):
    try:
        categories = dict(Category.objects.values_list('id', 'name'))
        company_info = CompanyService.get_company_info()
        customer_interests = [categories[interest] for interest in interests if interest in categories]
        
        
        object_content =_('LeBonPlanTEXAS : validation de devis')

        email_body = {
            'company_name' : company_info.name,
            'customer' : customer,
            'texas_trip': texas_trip,
            'trips' : trips,
            'interests' : customer_interests,
            'trip_invoice': invoice,
        }

        # Render the email template with context data
        subject = object_content
        from_email = company_info.email
        to_email = company_info.email
        bcc_email = [company_info.email] 
        text_content = 'Your email client does not support HTML content'

        html_email_content = render_to_string('email/estimate_validation_email.html', email_body)

        # Create the email message
        email = EmailMultiAlternatives(subject, text_content, from_email, [to_email], bcc=bcc_email)
        email.attach_alternative(html_email_content, 'text/html')

        # attach picture to email
        email = attach_pic_to_email(email)

        # Send the email
        email.send()
    except Exception as e:
        print('estimate_validation email error:', {e})
