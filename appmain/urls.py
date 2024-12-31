

from django.urls import path

from .views.register_view import multi_step_form
from .views.index_view import index
from .views.identiy import identity
from .views.privacy import privacy


urlpatterns = [
    path('index/', index, name='index'), 
    path('privacy_policy/', privacy, name='privacy'), 
    path('identity/', identity, name='identity'), 
    path('register/', multi_step_form, name='multi_step_form'), 
    path('thanku/', multi_step_form, name='success'), 
 ]
