# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/admin.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.contrib import admin,messages

from .models import Customer, Trip, Category, Interest, Invoice,FileForImage,Attraction,ImageDisplayTheme,CompanyInfo
from .models.texas_trip import TexasTrip
from .services.send_email import send_payment_link
from .services.invoice_service import InvoiceService
from .services.customer_service import CustumerService
from .services.company_service import CompanyService


# COMPANY PART
@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name','EIN','SIREN','legal_structure','address','tax_info','tax_math','email','phone','instagram','is_in_texas',)

# CUSTOMER PART
# Inline pour les Intérêts liés à un Customer
class InterestInline(admin.TabularInline):  # Ou `StackedInline` pour une disposition différente
    model = Interest
    extra = 1  # Nombre d'instances vides à afficher par défaut (1 par exemple)
    fields = ('category',)  # Remplacez par les champs d'Interest que vous souhaitez afficher

class TexasTripInline(admin.TabularInline):
    model = TexasTrip
    extra = 1
    fields = ('id', 'package',)

# Inline pour les Trips liés à un Customer
class TripInline(admin.TabularInline):  # Ou `StackedInline` pour une disposition différente
    model = Trip
    extra = 1  # Nombre d'instances vides à afficher par défaut (1 par exemple)
    fields = ('start_date','end_date','cities','comment','vehiculed','is_done')  # Remplacez par les champs de Trip que vous souhaitez afficher

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone','country', 'timestamp', 'selected_categories', 'is_called', 'is_mailed', 'is_done')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('email',)
    inlines = [InterestInline, TripInline,TexasTripInline] # Affichage des objets liés dans l'admin du Customer
    

# INVOICE PART
@admin.action(description="Envoyer un e-mail à l'utilisateur")
def send_email_action(modeladmin, request, queryset):
    success_count = 0
    error_count = 0

    for invoice in queryset:
        try:
            success,invoice = InvoiceService().create_token(invoice)
            if not success:
                modeladmin.message_user(request, "Problème lors de l'envoi des emails.", level="error")
            customer = invoice.customer
            if send_payment_link(customer, invoice):    
                success_count += 1
                CustumerService.customer_is_mailed(customer)
            else:
                error_count += 1
        except Exception as e:
            error_count += 1


    if success_count:
        modeladmin.message_user(request, f"{success_count} e-mails envoyés avec succès.", level=messages.SUCCESS)
    if error_count:
        modeladmin.message_user(request, f"Échec pour {error_count} e-mails.", level=messages.ERROR)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    readonly_fields = ('invoice_number',)
    list_display = ('customer','texas_trip','mobile_service','nbr_days_mobile',
        'mobile_price_excl_tax','driver_service', 'nbr_days_driver', 'driver_price_excl_tax', 
        'platinum_service', 'nbr_days_platinum', 'platinum_price_excl_tax',
        'tax_amount','total_excl_tax','total','terms_of_sale_accepted', 'is_paid')
    search_fields = ('customer', 'total','invoice_number')
    list_filter = ('customer','tax_amount','total_excl_tax','total',)
    actions = [send_email_action] 

    

# Enregistrement des autres modèles
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


#########################################
# ADVERTISSEMENT PART

@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = ('title','description','image_url')

# Inline pour les Trips liés à un Customer
class AttrictionInline(admin.TabularInline):  
    model = Attraction
    extra = 1  
    fields = ('title','description','image_url') 


# enregistrement  model FilForImage
@admin.register(FileForImage)
class FileForImageAdmin(admin.ModelAdmin):
    list_display = ('file_name','is_active')
    inlines = [AttrictionInline]

@admin.register(ImageDisplayTheme)
class ImageDisplayTheme(admin.ModelAdmin):
    list_display = ('theme','is_active')