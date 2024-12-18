# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/customer.py
# Author : Morice
# ---------------------------------------------------------------------------


from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from ..forms.customer_form import CustomerForm
from ..forms.trip_form import TripForm
from ..models import Category
from ..services.customer_service import CustumerService
from ..services.trip_service import TripService

def multi_step_form(request):
    step = request.session.get('step', 1) 

    if step == 1:
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            request.session['customer_data'] = form.cleaned_data
            request.session['step'] = 2
            return redirect('multi_step_form')

    elif step == 2:
        form = TripForm(request.POST or None)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            # Converting dates 
            for key, value in cleaned_data.items():
                if isinstance(value, date):
                    cleaned_data[key] = value.isoformat() 
            request.session['trip_data'] = form.cleaned_data
            request.session['step'] = 3
            return redirect('multi_step_form')

    elif step == 3:
        categories = Category.objects.all()
        if request.method == "POST":
            # Creating customer part (return the id and a boolean)
            custumer_data = request.session.get('customer_data')
            customer_id, success = CustumerService.create_custumer(custumer_data)
            if success:
                messages.success(request, _('Vos données personnelles ont bien été enregistrées'))
            else:
                messages.error(request, _("Une erreur s'est produite merci de recommencer"))
                request.session.flush()
                return redirect('multi_step_form')
            
            # Creating Trip part
            trip_data = request.session.get('trip_data')
            success = TripService.create_trip(trip_data,customer_id)
            if success:
                messages.success(request, _('Le voyage a bien été enregistré'))
            else:
                messages.error(request, _("Une erreur s'est produite merci de recommencer"))
                request.session.flush()
                return redirect('multi_step_form')
        
            # Creating Categories part
            selected_categories = request.POST.getlist('categories')  # Liste des IDs sélectionnés
            print("Catégories sélectionnées :", selected_categories)
            request.session['selected_categories'] = selected_categories
            request.session.flush()
            return redirect('success')

        return render(request, 'lebonplantexas/register_form.html', {'step': step, 'categories': categories})

    else:
        request.session['step'] = 1
        return redirect('multi_step_form')

    return render(request, 'lebonplantexas/register_form.html', {'step': step, 'form': form})
