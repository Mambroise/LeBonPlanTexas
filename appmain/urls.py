

from django.urls import path

from .views.register_view import multi_step_form
from .views.index_view import index


urlpatterns = [
    path('index/', index, name='index'), 
    path('register/', multi_step_form, name='multi_step_form'), 
    path('thanku/', multi_step_form, name='success'), 
 ]
