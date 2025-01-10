# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/signals.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.conf import settings
from .models import Invoice

@receiver(post_save, sender=Invoice)
def calculate_invoice_totals(sender, instance, created, **kwargs):
    # Calcul des totaux seulement si une modification ou une création a eu lieu
    if created or any([
        instance.mobile_service,
        instance.driver_service,
        instance.platinum_service
    ]):
        # Récupération des données nécessaires depuis l'instance
        mobile_total = (instance.nbr_days_mobile or 0) * (instance.mobile_price_excl_tax or 0) if instance.mobile_service else 0
        driver_total = (instance.nbr_days_driver or 0) * (instance.driver_price_excl_tax or 0) if instance.driver_service else 0
        platinum_total = (instance.nbr_days_platinum or 0) * (instance.platinum_price_excl_tax or 0) if instance.platinum_service else 0

        # Calcul des totaux
        total_excl_tax = mobile_total + driver_total + platinum_total
        tax_rate = float(settings.COMPANY_INFO['tva_info'].strip('%')) / 100  # Convertir le taux TVA en décimal
        tax_amount = round(total_excl_tax * tax_rate, 2)
        total_incl_tax = total_excl_tax + tax_amount

        # Mettre à jour l'instance
        instance.total_excl_tax = total_excl_tax
        instance.tax_rate = tax_rate
        instance.tax_amount = tax_amount
        instance.total = total_incl_tax

        # Sauvegarde pour appliquer les calculs
        Invoice.objects.filter(pk=instance.pk).update(
            total_excl_tax=total_excl_tax,
            tax_rate=tax_rate,
            tax_amount=tax_amount,
            total=total_incl_tax
        )

@receiver(post_save, sender=Invoice)
def set_invoice_number(sender, instance, created, **kwargs):
    if created and not instance.invoice_number:
        today_str = now().strftime('%Y%m%d')
        Invoice.objects.filter(pk=instance.pk).update(
            invoice_number=f"{instance.pk}{instance.customer.id}{today_str}"
        )