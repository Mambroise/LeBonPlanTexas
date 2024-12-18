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
from ..services.interest_service import InterestService

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
                return redirect('multi_step_form')  # Retourne à l'étape 2 pour une nouvelle entrée
            elif "finish_trips" in request.POST:
                request.session['step'] = 3
                return redirect('multi_step_form')

    elif step == 3:
        categories = Category.objects.all()
        if request.method == "POST":
            # Étape 3.1 : Création du client
            customer_data = request.session.get('customer_data')
            customer_id, success = CustumerService.create_custumer(customer_data)
            if not success:
                messages.error(request, _("Une erreur s'est produite lors de l'enregistrement du client."))
                request.session.flush()
                return redirect('multi_step_form')

            # Étape 3.2 : Création des voyages
            trip_data = request.session.get('trip_data', [])
            for trip in trip_data:
                success = TripService.create_trip(trip, customer_id)
                if not success:
                    messages.error(request, _("Une erreur s'est produite lors de l'enregistrement d'un voyage."))
                    request.session.flush()
                    return redirect('multi_step_form')

            # Étape 3.3 : Création des intérêts
            raw_categories = request.POST.getlist('categories')
            if len(raw_categories) == 1 and ',' in raw_categories[0]:
                raw_categories = raw_categories[0].split(',')

            try:
                selected_categories = [int(cat_id) for cat_id in raw_categories if cat_id.isdigit()]
            except ValueError:
                messages.error(request, _("Les catégories sélectionnées sont invalides."))
                return redirect('multi_step_form')

            success = InterestService.create_customer_interests(selected_categories, customer_id)
            if not success:
                messages.error(request, _("Une erreur s'est produite lors de l'enregistrement des catégories."))
                CustumerService.delete_customer(customer_id)
                request.session.flush()
                return redirect('multi_step_form')

            # Final success
            messages.success(request, _('Enregistrement terminé avec succès.'))
            request.session.flush()
            return redirect('success')

        return render(request, 'lebonplantexas/register_form.html', {'step': step, 'categories': categories})

    else:
        request.session['step'] = 1
        return redirect('multi_step_form')

    return render(request, 'lebonplantexas/register_form.html', {'step': step, 'form': form})
