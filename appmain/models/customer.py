# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/customer.py
# Author : Morice
# ---------------------------------------------------------------------------

import re
from django_countries.fields import CountryField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django import forms

# Create your models here.
class Customer(models.Model):

    first_name = models.CharField(_('Prénom'), max_length=100)
    last_name = models.CharField(_('Nom'), max_length=150)
    email = models.CharField(_('Email'), max_length=150)
    phone = models.CharField(_('Portable'),max_length=12, blank=True, null=True)
    address = models.CharField(_('Adresse'),max_length=200,null=True,blank=True)
    country = CountryField(blank_label=_('Pays'), null=False, blank=False)
    sign_up_number = models.CharField(max_length=100, unique=True,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    is_called = models.BooleanField(default=False)
    is_mailed = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)

    def selected_categories(self):
        return ", ".join(interest.category.name for interest in self.interests.select_related('category'))

    selected_categories.short_description = _('Catégories sélectionnées')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
    def clean(self):
        cleaned_data = super().clean()

        # Validation du numéro de téléphone : autoriser chiffres, espaces, tirets, parenthèses, et signe plus
        phone = self.phone
        
        if phone:
            # Supprimer les espaces, tirets, parenthèses et signes plus
            cleaned_phone = re.sub(r'[^0-9]', '', phone)
            
            # Vérifier la longueur du numéro après nettoyage
            if len(cleaned_phone) < 8 or len(cleaned_phone) > 12:
                raise ValidationError(_('Le numéro de téléphone doit comporter entre 8 et 12 chiffres.'))

            # Vérifier que le numéro ne contient que des chiffres (après nettoyage)
            if not cleaned_phone.isdigit():
                raise ValidationError(_('Le numéro de téléphone doit comporter uniquement des chiffres après nettoyage.'))

        return cleaned_data
    def clean_country(self):
        country = self.cleaned_data.get('country')
        if not country:
            raise forms.ValidationError(_("Veuillez sélectionner un pays."))
        return country
