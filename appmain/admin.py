# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/admin.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.conf import settings
from django.contrib import admin

from .models import Customer, Trip, Category, Interest, Invoice
from .models.texas_trip import TexasTrip
from .services.send_email import send_payment_link

# Inline pour les Intérêts liés à un Customer
class InterestInline(admin.TabularInline):  # Ou `StackedInline` pour une disposition différente
    model = Interest
    extra = 1  # Nombre d'instances vides à afficher par défaut (1 par exemple)
    fields = ('category',)  # Remplacez par les champs d'Interest que vous souhaitez afficher

class TexasTripInline(admin.TabularInline):
    model = TexasTrip
    extra = 1
    fields = ('created_at',)

# Inline pour les Trips liés à un Customer
class TripInline(admin.TabularInline):  # Ou `StackedInline` pour une disposition différente
    model = Trip
    extra = 1  # Nombre d'instances vides à afficher par défaut (1 par exemple)
    fields = ('start_date','end_date','cities','comment','vehiculed','is_done')  # Remplacez par les champs de Trip que vous souhaitez afficher

@admin.action(description="Envoyer un e-mail à l'utilisateur")
def send_email_action(modeladmin, request, queryset):
    for customer in queryset:
        print(customer)
        # subject = "Un message de Le Bon Plan Texas"
        # message = f"Bonjour {customer.first_name},\n\nVoici un message personnalisé pour vous."
        # from_email = settings.DEFAULT_FROM_EMAIL
        # recipient_list = [customer.email]
        
        # send_mail(subject, message, from_email, recipient_list)
        send_payment_link()
    
    modeladmin.message_user(request, "E-mails envoyés avec succès.")

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'timestamp', 'selected_categories')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('email',)
    inlines = [InterestInline, TripInline,TexasTripInline] # Affichage des objets liés dans l'admin du Customer
    

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('customer','texas_trip','mobile_service','nbr_days_mobile',
        'price_mobile','driver_service', 'nbr_days_driver', 'price_driver', 
        'platinum_service', 'nbr_days_platinum', 'price_platinum','total', 
        'payment_type', 'status')
    search_fields = ('customer', 'texas_trip', 'total')
    list_filter = ('customer',)
    actions = [send_email_action] 
    
# Enregistrement des autres modèles
admin.site.register(Category)

