# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/register_view.py
# Author : Morice
# ---------------------------------------------------------------------------


from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from ..forms.customer_form import CustomerForm
from ..forms.trip_form import TripForm
from ..models import Category,Price
from ..services import TripService,DiscountService,PriceService
from ..services import CustomerService, TexasTripService,InvoiceService,InterestService
from ..forms.texas_trip_form import TexasTripForm
from ..forms.discount_form import DiscountForm

from ..services.send_email import success_registration_email,send_payment_link

def multi_step_form(request):
    step = request.session.get('step', 1) 
    title = request.session.get('title', str(_('Choisir une formule'))) 
    package = request.session.get('texas_trip',{}).get('package')
    pckg_auto = None
    pckg_driver = None
    pckg_plat = None

    if step == 1:
        form = TexasTripForm(request.POST or None)
        # preparing package availability context for html cards
        pckg_auto, pckg_driver, pckg_plat = PriceService.get_active_prices()

        if form.is_valid():
            try:
                request.session['texas_trip'] = form.cleaned_data
                request.session['step'] = 2
                request.session['title'] = str(_('Entrez vos coordonnées'))
                return redirect('multi_step_form')
                
            except Exception as e:
                print(f'error in register_view, texas_trip part, step1 : {e}')
                messages.error(request,_('A problem occured. Please try again or contact us'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")


    elif step == 2:
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            request.session['customer_data'] = form.cleaned_data
            request.session['step'] = 3
            request.session['title'] = str(_('Détails du voyage'))
            package = request.session.get('texas_trip')
            # messages.info(request,_('Divisez votre voyages en plusieurs étapes en fonction des villes où vous resterez!'))
            return redirect('multi_step_form')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")


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
                request.session['title'] = str(_('Vos intérêts'))
                return redirect('multi_step_form')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")

    elif step == 4:
        form = DiscountForm(request.POST or None)

        categories = Category.objects.all().order_by('-id')
        if form.is_valid():
            code = form.cleaned_data.get('code')
            discount, message = DiscountService.find_valid_discount_by_code(code)
            if code and not discount:
                messages.error(request, message)
                return redirect('multi_step_form')
            if request.method == "POST":
                # Step 4.1 : Customer creation
                customer_data = request.session.get('customer_data')
                customer, success = CustomerService.create_customer(customer_data)
                if not success:
                    messages.error(request, _("Une erreur s'est produite lors de l'enregistrement des coordonnées."))
                    request.session.flush()
                    return redirect('multi_step_form')
                
                # Step 4.2 : TexasTrip creation
                texas_trip_data = request.session.get('texas_trip')
                texas_trip, success = TexasTripService.create_texas_trip(customer.id,texas_trip_data)
                if not success:
                    messages.error(request, _("Une erreur s'est produite lors de l'enregistrement de la formule."))
                    request.session.flush()
                    return redirect('multi_step_form')

                # Step 4.3 : Trip creation
                trip_data = request.session.get('trip_data', [])
                for trip in trip_data:
                    success = TripService.create_trip(trip, customer.id,texas_trip.id)
                    if not success:
                        messages.error(request, _("Une erreur s'est produite lors de l'enregistrement du voyage."))
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
                    CustomerService.delete_customer(customer.id)
                    request.session.flush()
                    return redirect('multi_step_form')

                # FINAL SUCCESS
                    # retreive all trips registered in the same texas_trip
                trips = texas_trip.whole_trips.all()
                    # send email to customer with trip summary
                success_registration_email(customer,texas_trip,trips,selected_categories)
                    # creation of invoice, only in autonomous service case
                success, invoice = InvoiceService.create_invoice(customer,trips,texas_trip,discount)
                    # send email to the client
                if success:
                    send_payment_link(customer=customer,invoice=invoice)
                    # estimate_validation(customer,texas_trip,trips,selected_categories,invoice)
                request.session.flush()
                return redirect('success', customer_id=customer.id)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")


        return render(request, 'lebonplantexas/register_form.html', {
            'step': step, 
            'categories': categories, 
            "title" : title, 
            "package": package,
            "form":form,
            "pckg_auto":pckg_auto,
            "pckg_driver":pckg_driver,
            "pckg_plat":pckg_plat,
            })

    else:
        request.session['step'] = 1
        return redirect('multi_step_form')

    return render(request, 'lebonplantexas/register_form.html', {
        'step': step,
        'form': form,
        "title" : title, 
        "package": package,
        "pckg_auto":pckg_auto,
        "pckg_driver":pckg_driver,
        "pckg_plat":pckg_plat,
        })


def reset_form(request):
    """Reinitialise forms after flushing session."""
    request.session.flush()
    messages.info(request,_("L'enregistrement a été abandonné"))
    return redirect('multi_step_form')

