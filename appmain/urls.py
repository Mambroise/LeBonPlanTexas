

from django.urls import path

from .views.register_view import multi_step_form


urlpatterns = [
    path('register/', multi_step_form, name='multi_step_form'), 
    path('thanku/', multi_step_form, name='success'), 
 ]
