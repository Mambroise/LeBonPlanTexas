# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/admin.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.contrib import admin
from .models import Customer, Trip, Category, Interest

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('email',)

admin.site.register(Trip)
admin.site.register(Category)
admin.site.register(Interest)
