# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/service/send_email.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from decouple import config
from django.conf import settings
import os
from email.mime.image import MIMEImage

from ..models import Customer,Invoice,Category

def send_payment_link(customer: Customer,invoice:Invoice):
    try:
        object_content = _('LeBonPlanTexas : DEVIS pour votre voyage!')
        payment_url_with_token = 'http://127.0.0.1:8000/payment/?token=' + invoice.token


        email_body = { 
            'company_info': settings.COMPANY_INFO,
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

        # attach picture to email
        email = attach_pic_to_email(email)

        # Send the email
        email.send()
        return True
        
    except Exception as e:
        print('erreurs', {e})
        return False

    

def success_registration_email(customer, trips, interests):
    try:
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
        from_email = config('EMAIL_HOST_USER')
        to_email = customer.email
        bcc_email = [settings.COMPANY_INFO['my_email']] 
        text_content = 'Your email client does not support HTML content'

        html_payment_link_content = render_to_string('email/success_registration_email.html', email_body)

        # Create the email message
        email = EmailMultiAlternatives(subject, text_content, from_email, [to_email], bcc=bcc_email)
        email.attach_alternative(html_payment_link_content, 'text/html')

        # attach picture to email
        email = attach_pic_to_email(email)

        # Send the email
        email.send()
    except Exception as e:
        print(f'erreur dans l\'envoi du mail de registration: {e}')


def send_checkout_success_email(invoice):
    try:
        # Objet de l'email
        subject = _('LeBonPlanTexas : Votre paiement est confirmé!')
        from_email = settings.EMAIL_HOST_USER  
        to_email = invoice.customer.email
        bcc_email = [settings.COMPANY_INFO['my_email']] 
        text_content = 'Your email client does not support HTML content'
        
        # Contenu du template HTML
        email_body = {
            'company_info': settings.COMPANY_INFO,
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