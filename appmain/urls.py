

from django.urls import path

from .views.register_view import multi_step_form
from .views.index_view import index
from .views.contact_view import contact
from .views.privacy_view import privacy
from .views.payment_view import payment_view
from .views.stripe_checkout_view import create_checkout_session
from .views.validate_terms_view import validate_terms
from .views.checkout_suc_can import checkout_success,checkout_cancelled
from .views.service_view import service_view
from .views.ajax_activities_view import get_activities
from .views.register_view import multi_step_form,reset_form
from .views.register_success_view import register_success
from .views.PDF_view import terms_of_sale_pdf,invoice_pdf

urlpatterns = [
    path('', index, name='index'), 
    path('get_activities/', get_activities, name='get_activities'), 
    path('privacy_policy/', privacy, name='privacy'), 
    path('contact/', contact, name='contact'), 
    path('services/', service_view, name='services'), 
    path('register/', multi_step_form, name='multi_step_form'), 
    path('reset-form/', reset_form, name='reset_form'),
    path('payment/', payment_view, name='payment_view'), 
    path('validate_terms/', validate_terms, name='validate_terms'), 
    path('terms_of_sale_pdf/', terms_of_sale_pdf, name='terms_of_sale_pdf'), 
    path('create-checkout-session/', create_checkout_session, name='create-checkout-session'), 
    path('checkout-success/', checkout_success, name='checkout_success'), 
    path('checkout-cancelled/', checkout_cancelled, name='checkout_cancelled'), 
    path('invoice_pdf/<int:invoice_id>/', invoice_pdf, name='invoice_pdf'),
    path('thanku/<int:customer_id>', register_success, name='success'), 
 ]
