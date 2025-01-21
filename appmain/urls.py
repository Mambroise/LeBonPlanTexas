

from django.urls import path

from .views.register_view import multi_step_form
from .views.index_view import index
from .views.contact_view import contact
from .views.privacy import privacy
from .views.payment_view import payment_view
from .views.stripe_checkout_view import create_checkout_session
from .views.validate_terms_view import validate_terms
from .views.checkout_suc_can import checkout_success,checkout_cancelled
from .views.checkout_suc_can import print_invoice
from .views.service_view import service_view
from .views.ajax_activities_view import get_activities

urlpatterns = [
    path('index/', index, name='index'), 
    path('get_activities/', get_activities, name='get_activities'), 
    path('privacy_policy/', privacy, name='privacy'), 
    path('contact/', contact, name='contact'), 
    path('services/', service_view, name='services'), 
    path('register/', multi_step_form, name='multi_step_form'), 
    path('payment/', payment_view, name='payment_view'), 
    path('validate_terms/', validate_terms, name='validate_terms'), 
    path('create-checkout-session/', create_checkout_session, name='create-checkout-session'), 
    path('checkout-success/', checkout_success, name='checkout_success'), 
    path('checkout-cancelled/', checkout_cancelled, name='checkout_cancelled'), 
    path('print_invoice/<int:invoice_id>/', print_invoice, name='print_invoice'),
    path('thanku/', multi_step_form, name='success'), 
 ]
