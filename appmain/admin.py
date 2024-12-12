# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/admin.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.contrib import admin
from .models import Customer, Trip, Category, Interest

# Inline pour les Intérêts liés à un Customer
class InterestInline(admin.TabularInline):  # Ou `StackedInline` pour une disposition différente
    model = Interest
    extra = 1  # Nombre d'instances vides à afficher par défaut (1 par exemple)
    fields = ('interest_field',)  # Remplacez par les champs d'Interest que vous souhaitez afficher

# Inline pour les Trips liés à un Customer
class TripInline(admin.TabularInline):  # Ou `StackedInline` pour une disposition différente
    model = Trip
    extra = 1  # Nombre d'instances vides à afficher par défaut (1 par exemple)
    fields = ('trip_field',)  # Remplacez par les champs de Trip que vous souhaitez afficher

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'timestamp')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('email',)
    inlines = [InterestInline, TripInline]  # Affichage des objets liés dans l'admin du Customer

# Enregistrement des autres modèles
admin.site.register(Category)

