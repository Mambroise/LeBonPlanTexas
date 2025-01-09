

from django.urls import path

from .views.register_view import multi_step_form
from .views.index_view import index
from .views.identiy import identity
from .views.privacy import privacy
from .views.payment_view import payment_view
from .views.stripe_checkout_view import create_checkout_session
from .views.validate_terms_view import validate_terms
from .views.checkout_suc_can import checkout_success,checkout_cancelled

urlpatterns = [
    path('index/', index, name='index'), 
    path('privacy_policy/', privacy, name='privacy'), 
    path('identity/', identity, name='identity'), 
    path('register/', multi_step_form, name='multi_step_form'), 
    path('payment/', payment_view, name='payment_view'), 
    path('validate_terms/', validate_terms, name='validate_terms'), 
    path('create-checkout-session/', create_checkout_session, name='create-checkout-session'), 
    path('checkout-success/', checkout_success, name='checkout_success'), 
    path('checkout-cancelled/', checkout_cancelled, name='checkout_cancelled'), 
    path('thanku/', multi_step_form, name='success'), 
 ]
