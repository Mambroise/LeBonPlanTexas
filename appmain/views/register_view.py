# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/register_view2.py
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
from ..services.interest_service import InterestService
from ..services.texas_trip_service import TexasTripService
from ..forms.texas_trip_form import TexasTripForm

from ..services.send_email import success_registration_email

def multi_step_form(request):
    step = request.session.get('step', 1) 
    title = request.session.get('title', 'Choisir une formule')  

    if step == 1:
        form = TexasTripForm(request.POST or None)
        if form.is_valid():
            try:
                request.session['texas_trip'] = form.cleaned_data
                request.session['step'] = 2
                request.session['title'] = 'Entrez vos coordonnées'
                return redirect('multi_step_form')
                
            except Exception as e:
                print(f'error in register_view, texas_trip part, step1 : {e}')

    elif step == 2:
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            request.session['customer_data'] = form.cleaned_data
            request.session['step'] = 3
            request.session['title'] = 'Détails du voyage'
            return redirect('multi_step_form')

    elif step == 3:
        form = TripForm(request.POST or None)

        if form.is_valid():
            cleaned_data = {
                key: (value.isoformat() if isinstance(value, date) else value)
                for key, value in form.cleaned_data.items()
            }

            # Ajouter les données de cette étape de voyage à la liste
            trip_data = request.session.get('trip_data', [])
            trip_data.append(cleaned_data)
            request.session['trip_data'] = trip_data

            # Vérifier quel bouton a été utilisé
            if "add_trip" in request.POST:
                messages.success(request, _("L'étape de voyage a été ajoutée. Vous pouvez en ajouter une autre."))
                return redirect('multi_step_form') 
            elif "finish_trips" in request.POST:
                request.session['step'] = 4
                request.session['title'] = 'Vos intérêts'
                return redirect('multi_step_form')

    elif step == 4:
        categories = Category.objects.all().order_by('-id')
        # translate categories according to language
        translated_categories = [
            {'id': category.id, 'name': category.get_translated_name()}
            for category in categories
        ]

        if request.method == "POST":
            # Step 4.1 : Customer creation
            customer_data = request.session.get('customer_data')
            customer, success = CustumerService.create_custumer(customer_data)
            if not success:
                messages.error(request, _("Une erreur s'est produite lors de l'enregistrement du client."))
                request.session.flush()
                return redirect('multi_step_form')
            
            # Step 4.2 : TexasTrip creation
            texas_trip_data = request.session.get('texas_trip')
            texas_trip, success = TexasTripService.create_texas_trip(customer.id,texas_trip_data)
            if not success:
                messages.error(request, _("Une erreur s'est produite lors de l'enregistrement du client."))
                request.session.flush()
                return redirect('multi_step_form')

            # Step 4.3 : Trip creation
            trip_data = request.session.get('trip_data', [])
            for trip in trip_data:
                success = TripService.create_trip(trip, customer.id,texas_trip.id)
                if not success:
                    messages.error(request, _("Une erreur s'est produite lors de l'enregistrement d'un voyage."))
                    request.session.flush()
                    return redirect('multi_step_form')

            # Step 4.4 : Interests creation
            raw_categories = request.POST.getlist('categories')
            if len(raw_categories) == 1 and ',' in raw_categories[0]:
                raw_categories = raw_categories[0].split(',')

            try:
                selected_categories = [int(cat_id) for cat_id in raw_categories if cat_id.isdigit()]
            except ValueError:
                messages.error(request, _("Les catégories sélectionnées sont invalides."))
                return redirect('multi_step_form')

            success = InterestService.create_customer_interests(selected_categories, customer.id)
            if not success:
                messages.error(request, _("Une erreur s'est produite lors de l'enregistrement des catégories."))
                CustumerService.delete_customer(customer.id)
                request.session.flush()
                return redirect('multi_step_form')

            # Final success
            trips = texas_trip.whole_trips.all()
            success_registration_email(customer,trips,selected_categories)
            messages.success(request, _('Enregistrement terminé avec succès.'))
            request.session.flush()
            return redirect('success')

        return render(request, 'lebonplantexas/register_form.html', {'step': step, 'categories': translated_categories, "title" : title})

    else:
        request.session['step'] = 1
        return redirect('multi_step_form')

    return render(request, 'lebonplantexas/register_form.html', {'step': step, 'form': form, "title" : title})
